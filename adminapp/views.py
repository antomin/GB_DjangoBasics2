from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from adminapp.forms import (ProductCategoryCreateForm,
                            ProductCreationAdminForm, ShopUserCreateAdminForm,
                            ShopUserEditAdminForm)
from authapp.models import ShopUser
from mainapp.mixin import AddContextMixin, SuperUserRequiredMixin
from mainapp.models import Product, ProductCategory


class Index(TemplateView, AddContextMixin, SuperUserRequiredMixin):
    template_name = 'adminapp/admin.html'
    title = 'Панель администратора'


class ShopUserListView(ListView, AddContextMixin, SuperUserRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/shopuser_list.html'
    title = 'Пользователи'


class ShopUserCreateView(CreateView, AddContextMixin, SuperUserRequiredMixin):
    model = ShopUser
    form_class = ShopUserCreateAdminForm
    template_name = 'adminapp/shopuser_create.html'
    success_url = reverse_lazy('admin:user_view')
    title = 'Новый пользователь'


class ShopUserUpdateView(UpdateView, AddContextMixin, SuperUserRequiredMixin):
    model = ShopUser
    form_class = ShopUserEditAdminForm
    template_name = 'adminapp/shopuser_update.html'
    success_url = reverse_lazy('admin:user_view')
    title = 'Редактирование пользователя'


class ShopUserDeleteView(DeleteView, AddContextMixin, SuperUserRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/shopuser_delete.html'
    success_url = reverse_lazy('admin:user_view')
    title = 'Удаление пользователя'


class ProductCategoryListView(ListView, AddContextMixin, SuperUserRequiredMixin):
    model = ProductCategory
    template_name = 'adminapp/productcategory_list.html'
    title = 'Категории'


class ProductCategoryCreateView(CreateView, AddContextMixin, SuperUserRequiredMixin):
    model = ProductCategory
    form_class = ProductCategoryCreateForm
    template_name = 'adminapp/productcategory_create.html'
    success_url = reverse_lazy('admin:category_view')
    title = 'Новая категория'


class ProductCategoryUpdateView(UpdateView, AddContextMixin, SuperUserRequiredMixin):
    model = ProductCategory
    form_class = ProductCategoryCreateForm
    template_name = 'adminapp/productcategory_edit.html'
    success_url = reverse_lazy('admin:category_view')
    title = 'Редактирование категории'


class ProductCategoryDeleteView(DeleteView, AddContextMixin, SuperUserRequiredMixin):
    model = ProductCategory
    template_name = 'adminapp/productcategory_delete.html'
    success_url = reverse_lazy('admin:category_view')
    title = 'Удаление категории'

# def category_delete(request, pk):
#     deleted_category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         deleted_category.is_active = False
#         deleted_category.save()
#         return HttpResponseRedirect(reverse('admin:category_view'))
#
#     context = {
#         'title': 'Удаление пользователя',
#         'deleted_category': deleted_category,
#     }
#
#     return render(request, 'adminapp/productcategory_delete.html', context)


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
