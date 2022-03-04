from django.shortcuts import render

from authapp.models import ShopUser


def index(request):
    return render(request, 'adminapp/admin.html')


def user_read(request):
    context = {
        'title': 'Пользователи',
        'users': ShopUser.objects.all(),
    }

    return render(request, 'adminapp/admin-users-read.html', context)


def user_create(request):
    return render(request, 'adminapp/admin-users-create.html')


def user_edit(request):
    return render(request, 'adminapp/admin-users-edit.html')


def user_delete(request, user_pk):
    return render(request, 'adminapp/admin-users-edit.html')
