from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
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
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.success(request, 'Проверьте почту.')
                return HttpResponseRedirect(reverse('auth:login'))
        return render(request, self.template_name, {'form': form})

    @staticmethod
    def send_verify_link(user):
        verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
        subject = f'Подтверждение регистрации пользователя {user.username}'
        message = f'Для подтверждения учетной записи {user.username} на портале {settings.DOMAIN_NAME} перейдите по ' \
                  f'ссылке:\n{settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if user and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = ''
            user.activation_key_expires = ''
            user.save()
            auth.login(request, user)
        return render(request, 'authapp/verification.html')
    except Exception as e:
        print(e)
        HttpResponseRedirect(reverse('index'))


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
