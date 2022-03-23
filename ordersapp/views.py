from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from basketapp.models import Basket
from mainapp.models import Product
from ordersapp.forms import OrderItemForm
from ordersapp.models import Order, OrderItem


class OrdersList(LoginRequiredMixin, ListView):
    model = Order
    extra_context = {'title': 'Заказы'}

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrdersCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    extra_context = {'title': 'Оформление заказа'}

    def get_context_data(self, **kwargs):
        context = super(OrdersCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user=self.request.user)
            if basket_items:
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=len(basket_items))
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.price
                basket_items.delete()
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrdersCreate, self).form_valid(form)


class OrdersUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    extra_context = {'title': 'Редактирование заказа'}

    def get_context_data(self, **kwargs):
        context = super(OrdersUpdate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']
        with transaction.atomic():
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrdersUpdate, self).form_valid(form)


class OrdersDelete(LoginRequiredMixin, DeleteView):
    model = Order
    extra_context = {'title': 'Удаление заказа'}
    success_url = reverse_lazy('orders:list')


class OrdersDetail(LoginRequiredMixin, DetailView):
    model = Order
    extra_context = {'title': 'Подробности'}


def forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()
    return HttpResponseRedirect(reverse('orders:list'))


def get_price(request, pk):
    if request.is_ajax():
        product = get_object_or_404(Product, pk=pk)
        product_price = product.price if product.price else 0
        return JsonResponse({'price': product_price})


@receiver(pre_save, sender=Basket)
@receiver(pre_save, sender=OrderItem)
def product_quantity_update_save(sender, instance, **kwargs):
    if instance.pk:
        instance.product.quantity -= instance.quantity - sender.get_item(instance.pk).quantity
    else:
        instance.product.quantity -= instance.quantity
    instance.product.save()


@receiver(pre_delete, sender=Basket)
@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.product.save()
