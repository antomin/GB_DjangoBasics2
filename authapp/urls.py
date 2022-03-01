from django.urls import path

import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('registration/', authapp.registration, name='registration'),
    path('profile/', authapp.profile, name='profile'),
    path('logout/', authapp.logout, name='logout'),
]
