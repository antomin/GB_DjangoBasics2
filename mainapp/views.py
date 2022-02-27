from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'главная',
    }

    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)
