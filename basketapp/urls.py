from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('add/<int:product_pk>/', basketapp.basket_add, name='add'),
    path('remove/<int:basket_pk>/', basketapp.basket_remove, name='remove'),
    path('edit/<int:basket_pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]
