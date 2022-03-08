from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.Index.as_view(), name='index'),

    path('users/', adminapp.ShopUserListView.as_view(), name='user_view'),
    path('users/create/', adminapp.ShopUserCreateView.as_view(), name='user_create'),
    path('users/edit/<int:pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_edit'),
    path('users/delete/<int:pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/', adminapp.ProductCategoryListView.as_view(), name='category_view'),
    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/edit/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_edit'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/', adminapp.product_read, name='product_view'),
    path('products/create/', adminapp.product_create, name='product_create'),
    path('products/edit/<int:product_pk>/', adminapp.product_edit, name='product_edit'),
    path('products/delete/<int:product_pk>/', adminapp.product_delete, name='product_delete'),
]
