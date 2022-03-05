from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from adminapp.forms import (CategoryCreationAdminForm,
                            ProductCreationAdminForm, UserCreationAdminForm,
                            UserEditAdminForm)
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    context = {
        'title': 'Панель администратора'
    }
    return render(request, 'adminapp/admin.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_read(request):
    context = {
        'title': 'Пользователи',
        'users': ShopUser.objects.all()
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = UserCreationAdminForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:user_view'))
        else:
            print(form.errors)

    context = {
        'title': 'Новый пользователь',
        'form': UserCreationAdminForm(),
    }

    return render(request, 'adminapp/users_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, user_pk):
    edited_user = get_object_or_404(ShopUser, pk=user_pk)
    if request.method == 'POST':
        form = UserEditAdminForm(data=request.POST, instance=edited_user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:user_view'))
        else:
            print(form.errors)

    context = {
        'title': f'Редактирование пользователя {edited_user.username}',
        'form': UserEditAdminForm(instance=edited_user),
        'edited_user': edited_user
    }

    return render(request, 'adminapp/users_edit.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, user_pk):
    deleted_user = get_object_or_404(ShopUser, pk=user_pk)
    if request.method == 'POST':
        deleted_user.is_active = False
        deleted_user.save()
        return HttpResponseRedirect(reverse('admin:user_view'))

    context = {
        'title': 'Удаление пользователя',
        'deleted_user': deleted_user,
    }

    return render(request, 'adminapp/users_delete.html', context)


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
def product_edit(request):
    return render(request, 'adminapp/products_edit.html')


def product_delete(request, user_pk):
    return render(request, 'adminapp/products_delete.html')
