from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/view/', adminapp.user_read, name='user_view'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/edit/<int:user_pk>', adminapp.user_edit, name='user_edit'),
    path('users/delete/', adminapp.user_delete, name='user_delete'),
]
