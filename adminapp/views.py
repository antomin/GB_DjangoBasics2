from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, ListView,
                                  TemplateView, UpdateView)

from adminapp.forms import (ProductCategoryCreateForm, ProductCreateForm,
                            ShopUserCreateAdminForm, ShopUserEditAdminForm)
from authapp.models import ShopUser
from mainapp.mixin import AddContextMixin, SuperUserRequiredMixin
from mainapp.models import Product, ProductCategory


class Index(TemplateView, AddContextMixin, SuperUserRequiredMixin):
    template_name = 'adminapp/admin.html'
    title = 'Панель администратора'


class ShopUserListView(ListView, AddContextMixin, SuperUserRequiredMixin):
    model = ShopUser
    template_name = 'adminapp/shopuser_list.html'
    ordering = ['-is_active', 'name']
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
    ordering = ['-is_active', 'name']
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


class ProductListView(ListView, AddContextMixin, SuperUserRequiredMixin):
    model = Product
    template_name = 'adminapp/product_list.html'
    ordering = ['-is_active', 'name']
    title = 'Продукты'


class ProductCreateView(CreateView, AddContextMixin, SuperUserRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    template_name = 'adminapp/product_create.html'
    success_url = reverse_lazy('admin:product_view')
    title = 'Новый продукт'


class ProductUpdateView(UpdateView, AddContextMixin, SuperUserRequiredMixin):
    model = Product
    form_class = ProductCreateForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('admin:product_view')
    title = 'Редактирование продукта'


class ProductDeleteView(DeleteView, AddContextMixin, SuperUserRequiredMixin):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:product_view')
    title = 'Удаление продукта'

