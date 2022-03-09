from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from authapp.forms import (ShopUserEditForm, ShopUserLoginForm,
                           ShopUserRegistrationForm)
from authapp.models import ShopUser
from basketapp.models import Basket


class Login(LoginView):
    form_class = ShopUserLoginForm
    template_name = 'authapp/login.html'
    extra_context = {'title': 'вход'}


class Registration(CreateView):
    model = ShopUser
    form_class = ShopUserRegistrationForm
    template_name = 'authapp/registration.html'
    success_url = reverse_lazy('auth:login')
    extra_context = {'title': 'регистрация'}

    def post(self, request, *args, **kwargs):
        super(Registration, self).post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'Вы успешно зарегистрировались')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ProfileView(UpdateView, LoginRequiredMixin):
    model = ShopUser
    form_class = ShopUserEditForm
    template_name = 'authapp/profile.html'
    success_url = reverse_lazy('auth:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(ShopUser, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['basket'] = Basket.objects.filter(user=self.request.user)
        context['title'] = 'профиль'
        return context

    def post(self, request, *args, **kwargs):
        super(ProfileView, self).post(request, *args, **kwargs)
        form = self.get_form()
        if form.is_valid():
            messages.set_level(request, messages.SUCCESS)
            messages.success(request, 'Данные обновлены')
            return self.form_valid(form)
        else:
            messages.error(request, list(form.errors.values())[0])
            return self.form_invalid(form)
