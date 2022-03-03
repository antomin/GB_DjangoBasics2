from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket_add(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, basket_pk, quantity):
    quantity = int(quantity)
    if request.is_ajax():
        new_basket = get_object_or_404(Basket, pk=basket_pk)

        if quantity > 0:
            new_basket.quantity = quantity
            new_basket.save()
        else:
            new_basket.delete()

        basket_items = Basket.objects.filter(user=request.user)

        context = {
            'basket': basket_items,
        }

        result = render_to_string('basketapp/inc_basket.html', context)

        return JsonResponse({'result': result})


@login_required
def basket_remove(request, basket_pk):
    basket = get_object_or_404(Basket, pk=basket_pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
