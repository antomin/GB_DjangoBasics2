from django.urls import path

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrdersList.as_view(), name='list'),
    path('create/', ordersapp.OrdersCreate.as_view(), name='create'),
    path('update/<int:pk>/', ordersapp.OrdersUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ordersapp.OrdersDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', ordersapp.OrdersDetail.as_view(), name='read'),
    path('complite/<int:pk>/', ordersapp.forming_complete, name='forming_complete'),
    path('get_price/<int:pk>/', ordersapp.get_price, name='get_price'),
]
