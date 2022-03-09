from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.ProductListView.as_view(), name='index'),
    path('<int:pk>/', mainapp.ProductDetailView.as_view(), name='product'),
    path('page/<int:pk>/', mainapp.ProductListView.as_view(), name='products'),
    # path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
]
