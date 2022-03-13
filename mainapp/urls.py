from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<int:pk>/', mainapp.ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>/', mainapp.products, name='products'),
    path('category/<int:pk>/page-<int:page>/', mainapp.products, name='page'),
]
