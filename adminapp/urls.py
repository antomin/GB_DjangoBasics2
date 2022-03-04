from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/view/', adminapp.user_read, name='user_view'),
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/update/', adminapp.user_update, name='user_update'),
    path('users/delete/', adminapp.user_delete, name='user_delete'),
]
