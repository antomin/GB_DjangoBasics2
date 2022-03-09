from django.contrib.auth.views import LogoutView
from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.Login.as_view(), name='login'),
    path('registration/', authapp.Registration.as_view(), name='registration'),
    path('profile/', authapp.ProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(template_name='mainapp/index.html'), name='logout'),
]
