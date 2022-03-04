from django.shortcuts import render

from authapp.models import ShopUser
from mainapp.models import ProductCategory


def index(request):
    return render(request, 'adminapp/admin.html')


def user_read(request):
    context = {
        'title': 'Пользователи',
        'users': ShopUser.objects.all().order_by('-is_active', '-is_staff', 'username'),
    }

    return render(request, 'adminapp/users.html', context)


def user_create(request):
    return render(request, 'adminapp/users_create.html')


def user_edit(request):
    return render(request, 'adminapp/users_edit.html')


def user_delete(request, user_pk):
    return render(request, 'adminapp/users_edit.html')


def category_read(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategory.objects.all().order_by('-is_active', 'name'),
    }

    return render(request, 'adminapp/categories.html', context)


def category_create(request):
    return render(request, 'adminapp/categories_create.html')


def category_edit(request):
    return render(request, 'adminapp/categories_edit.html')


def category_delete(request):
    return render(request, 'adminapp/categories_delete.html')


def product_read(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategory.objects.all().order_by('-is_active', 'name'),
    }

    return render(request, 'adminapp/products.html', context)


def product_create(request):
    return render(request, 'adminapp/products_create.html')


def product_edit(request):
    return render(request, 'adminapp/products_edit.html')


def product_delete(request, user_pk):
    return render(request, 'adminapp/products_delete.html')
