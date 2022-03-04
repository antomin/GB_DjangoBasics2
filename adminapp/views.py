from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminapp.forms import UserCreationAdminForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def user_read(request):
    context = {
        'title': 'Пользователи',
        'users': ShopUser.objects.all().order_by('-is_active', '-is_staff', 'username'),
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
            print(form.error)
    else:
        form = UserCreationAdminForm()

    context = {
        'title': 'Новый пользователь',
        'form': form,
    }

    return render(request, 'adminapp/users_create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request):
    return render(request, 'adminapp/users_edit.html')


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, user_pk):
    return render(request, 'adminapp/users_edit.html')


@user_passes_test(lambda u: u.is_superuser)
def category_read(request):
    context = {
        'title': 'Категории',
        'categories': ProductCategory.objects.all().order_by('-is_active', 'name'),
    }

    return render(request, 'adminapp/categories.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    return render(request, 'adminapp/categories_create.html')


@user_passes_test(lambda u: u.is_superuser)
def category_edit(request):
    return render(request, 'adminapp/categories_edit.html')


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request):
    return render(request, 'adminapp/categories_delete.html')


@user_passes_test(lambda u: u.is_superuser)
def product_read(request):
    context = {
        'title': 'Все продукты',
        'products': Product.objects.all().order_by('-is_active', '-category__name', 'name'),
    }

    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request):
    return render(request, 'adminapp/products_create.html')


@user_passes_test(lambda u: u.is_superuser)
def product_edit(request):
    return render(request, 'adminapp/products_edit.html')


def product_delete(request, user_pk):
    return render(request, 'adminapp/products_delete.html')
