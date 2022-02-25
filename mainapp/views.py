from django.shortcuts import render


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'каталог',
    }
    return render(request, 'mainapp/products.html', context)
