from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from adminapp.forms import (OrderEditForm, ProductCategoryCreateForm,
                            ProductCreateForm, ShopUserCreateAdminForm,
                            ShopUserEditAdminForm)
from authapp.models import ShopUser
from mainapp.mixin import SuperUserRequiredMixin
from mainapp.models import Product, ProductCategory
from ordersapp.models import Order


class Index(TemplateView, SuperUserRequiredMixin):
    template_name = 'adminapp/admin.html'
    extra_context = {'title': 'Панель администратора'}


class ShopUserListView(ListView, SuperUserRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/shopuser_list.html'
    ordering = ['-is_active', 'name']
    extra_context = {'title': 'Пользователи'}


class ShopUserCreateView(CreateView, SuperUserRequiredMixin):
    model = ShopUser
    form_class = ShopUserCreateAdminForm
    template_name = 'adminapp/shopuser_create.html'
    success_url = reverse_lazy('admin:user_view')
    extra_context = {'title': 'Новый пользователь'}


class ShopUserUpdateView(UpdateView, SuperUserRequiredMixin):
    model = ShopUser
    form_class = ShopUserEditAdminForm
    template_name = 'adminapp/shopuser_update.html'
    success_url = reverse_lazy('admin:user_view')
    extra_context = {'title': 'Редактирование пользователя'}


class ShopUserDeleteView(DeleteView, SuperUserRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/shopuser_delete.html'
    success_url = reverse_lazy('admin:user_view')
    extra_context = {'title': 'Удаление пользователя'}


class ProductCategoryListView(ListView, SuperUserRequiredMixin):
    model = ProductCategory
    template_name = 'adminapp/productcategory_list.html'
    ordering = ['-is_active', 'name']
    extra_context = {'title': 'Категории'}


class ProductCategoryCreateView(CreateView, SuperUserRequiredMixin):
    model = ProductCategory
    form_class = ProductCategoryCreateForm
    template_name = 'adminapp/productcategory_create.html'
    success_url = reverse_lazy('admin:category_view')
    extra_context = {'title': 'Новая категория'}


class ProductCategoryUpdateView(UpdateView, SuperUserRequiredMixin):
    model = ProductCategory
    form_class = ProductCategoryCreateForm
    template_name = 'adminapp/productcategory_edit.html'
    success_url = reverse_lazy('admin:category_view')
    extra_context = {'title': 'Редактирование категории'}


class ProductCategoryDeleteView(DeleteView, SuperUserRequiredMixin):
    model = ProductCategory
    template_name = 'adminapp/productcategory_delete.html'
    success_url = reverse_lazy('admin:category_view')
    extra_context = {'title': 'Удаление категории'}


class ProductListView(ListView, SuperUserRequiredMixin):
    model = Product
    template_name = 'adminapp/product_list.html'
    ordering = ['-is_active', 'name']
    extra_context = {'title': 'Продукты'}


class ProductCreateView(CreateView, SuperUserRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('admin:product_view')
    extra_context = {'title': 'Новый продукт'}


class ProductUpdateView(UpdateView, SuperUserRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin:product_view')
    extra_context = {'title': 'Редактирование продукта'}


class ProductDeleteView(DeleteView, SuperUserRequiredMixin):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:product_view')
    extra_context = {'title': 'Удаление продукта'}


class OrderListView(ListView, SuperUserRequiredMixin):
    model = Order
    template_name = 'adminapp/order_list.html'
    ordering = ('-is_active',)
    extra_context = {'title': 'Заказы'}


class OrderListUpdate(UpdateView, SuperUserRequiredMixin):
    model = Order
    template_name = 'adminapp/order_update.html'
    form_class = OrderEditForm
    success_url = reverse_lazy('admin:order_view')
    extra_context = {'title': 'Редактирование заказа'}

