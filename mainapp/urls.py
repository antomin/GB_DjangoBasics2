from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('<int:product_pk>/', mainapp.product, name='product'),
    path('category/<int:category_pk>/', mainapp.products, name='products'),
]
