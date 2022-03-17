from django.urls import path

import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrdersListView.as_view(), name='list'),
    path('create/', ordersapp.OrdersCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ordersapp.OrdersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ordersapp.OrdersDeleteView.as_view(), name='delete'),
]
