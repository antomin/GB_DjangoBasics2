from django.urls import path

import basketapp.views as basketapp

app_name = 'basket'

urlpatterns = [
    path('add/<int:pk>', basketapp.add, name='add'),
    path('remove/<int:pk>', basketapp.remove, name='remove'),
]
