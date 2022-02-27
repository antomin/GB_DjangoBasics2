from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserRegistrationForm


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
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'вход',
        'form': form,
    }

    return render(request, 'authapp/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = ShopUserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = ShopUserRegistrationForm()

    context = {
        'title': 'регистрация',
        'form': form,
    }

    return render(request, 'authapp/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
