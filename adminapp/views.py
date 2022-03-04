from django.shortcuts import render


def index(request):
    return render(request, 'adminapp/admin.html')


def user_read(request):
    return render(request, 'adminapp/admin-users-read.html')


def user_create(request):
    return render(request, 'adminapp/admin-users-create.html')


def user_update(request):
    return render(request, 'adminapp/admin-users-update.html')


def user_delete(request):
    return render(request, 'adminapp/admin-users-update.html')
