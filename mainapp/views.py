from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'главная',
    }

    return render(request, 'mainapp/index.html', context)


# def products(request, category_pk=None):
#     if category_pk:
#         products_list = Product.objects.filter(category__pk=category_pk)
#     else:
#         products_list = Product.objects.all()
#
#     context = {
#         'title': 'каталог',
#         'categories': ProductCategory.objects.all(),
#         'products': products_list,
#         'basket': Basket.objects.filter(user=request.user),
#     }
#
#     return render(request, 'mainapp/products.html', context)

def products(request, category_pk=None):
    if category_pk:
        products_list = Product.objects.filter(category__pk=category_pk)
    else:
        products_list = Product.objects.all()

    if request.is_ajax():
        result = render_to_string(
            'mainapp/includes/inc_product_list.html',
            context={'products': products_list}
        )

        return JsonResponse({'result': result})

    context = {
        'title': 'каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_list,
        'basket': Basket.objects.filter(user=request.user),
    }

    return render(request, 'mainapp/products.html', context)


def product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    context = {
        'title': product.name,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)
