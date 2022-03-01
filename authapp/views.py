from django.contrib import auth, messages
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authapp.forms import (ShopUserEditForm, ShopUserLoginForm,
                           ShopUserRegistrationForm)


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))

    context = {
        'title': 'вход',
        'form': ShopUserLoginForm(),
    }

    return render(request, 'authapp/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = ShopUserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('auth:login'))

    context = {
        'title': 'регистрация',
        'form': ShopUserRegistrationForm()
    }

    return render(request, 'authapp/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = ShopUserEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Данные обновлены')
        else:
            print(form.errors)

    context = {
        'title': 'профиль',
        'form': ShopUserEditForm(instance=request.user)
    }
    return render(request, 'authapp/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
