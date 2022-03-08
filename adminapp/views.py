from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from adminapp.forms import (CategoryCreationAdminForm,
                            ProductCreationAdminForm, ShopUserCreateAdminForm,
                            ShopUserEditAdminForm)
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


class Index(TemplateView):
    template_name = 'adminapp/admin.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['title'] = 'Панель администратора'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(Index, self).dispatch(request, *args, **kwargs)


class ShopUserListView(ListView):
    model = ShopUser
    template_name = 'adminapp/shopuser_list.html'

    def get_context_data(self, **kwargs):
        context = super(ShopUserListView, self).get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ShopUserListView, self).dispatch(request, *args, **kwargs)


class ShopUserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserCreateAdminForm
    template_name = 'adminapp/shopuser_create.html'
    success_url = reverse_lazy('admin:user_view')

    def get_context_data(self, **kwargs):
        context = super(ShopUserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Новый пользователь'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ShopUserCreateView, self).dispatch(request, *args, **kwargs)


class ShopUserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserEditAdminForm
    template_name = 'adminapp/shopuser_update.html'
    success_url = reverse_lazy('admin:user_view')

    def get_context_data(self, **kwargs):
        context = super(ShopUserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ShopUserUpdateView, self).dispatch(request, *args, **kwargs)


class ShopUserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'adminapp/shopuser_delete.html'
    success_url = reverse_lazy('admin:user_view')

    def get_context_data(self, **kwargs):
        context = super(ShopUserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ShopUserDeleteView, self).dispatch(request, *args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def category_read(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategory.objects.all().order_by('-is_active', 'name'),
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        form = CategoryCreationAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:category_view'))
        else:
            print(form.errors)

    context = {
        'title': 'Новая категория',
        'form': CategoryCreationAdminForm()
    }

    return render(request, 'adminapp/categories_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_edit(request, category_pk):
    edited_category = get_object_or_404(ProductCategory, pk=category_pk)
    if request.method == 'POST':
        form = CategoryCreationAdminForm(data=request.POST, instance=edited_category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:category_view'))
        else:
            print(form.errors)

    context = {
        'title': f'Редактирование категории {edited_category.name}',
        'form': CategoryCreationAdminForm(instance=edited_category),
        'edited_category': edited_category
    }

    return render(request, 'adminapp/categories_edit.html', context)


def category_delete(request, category_pk):
    deleted_category = get_object_or_404(ProductCategory, pk=category_pk)
    if request.method == 'POST':
        deleted_category.is_active = False
        deleted_category.save()
        return HttpResponseRedirect(reverse('admin:category_view'))

    context = {
        'title': 'Удаление пользователя',
        'deleted_category': deleted_category,
    }

    return render(request, 'adminapp/categories_delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_read(request):
    context = {
        'title': 'Все продукты',
        'products': Product.objects.all().order_by('-is_active', '-category__name', 'name'),
    }

    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    if request.method == 'POST':
        form = ProductCreationAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:product_view'))
        else:
            print(form.errors)

    context = {
        'title': 'Новый продукт',
        'form': ProductCreationAdminForm(),
    }

    return render(request, 'adminapp/products_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_edit(request, product_pk):
    edited_product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = ProductCreationAdminForm(data=request.POST, instance=edited_product, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:product_view'))
        else:
            print(form.errors)

    context = {
        'title': f'Редактирование категории {edited_product.name}',
        'form': ProductCreationAdminForm(instance=edited_product),
        'edited_product': edited_product
    }

    return render(request, 'adminapp/products_edit.html', context)


def product_delete(request, product_pk):
    deleted_product = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        deleted_product.is_active = False
        deleted_product.save()
        return HttpResponseRedirect(reverse('admin:product_view'))

    context = {
        'title': 'Удаление пользователя',
        'deleted_product': deleted_product,
    }

    return render(request, 'adminapp/products_delete.html', context)
