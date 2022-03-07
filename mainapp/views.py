from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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


def products(request, pk=None, page=1):
    if pk:
        products_list = Product.objects.filter(category__pk=pk, is_active=True)
    else:
        products_list = Product.objects.filter(is_active=True, category__is_active=True)

    paginator = Paginator(products_list, 2)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': 'каталог',
        'categories': ProductCategory.objects.filter(is_active=True),
        'products': products_paginator,
        'basket': Basket.objects.filter(user=request.user),
    }

    return render(request, 'mainapp/products.html', context)

# def products(request, category_pk=None, page=1):
#     if category_pk:
#         products_list = Product.objects.filter(category__pk=category_pk, is_active=True)
#     else:
#         products_list = Product.objects.filter(is_active=True, category__is_active=True)
#
#     paginator = Paginator(products_list, 2)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#
#     if request.is_ajax():
#         result = render_to_string(
#             'mainapp/includes/inc_product_list.html',
#             context={'products': products_paginator}
#         )
#
#         return JsonResponse({'result': result})
#
#     context = {
#         'title': 'каталог',
#         'categories': ProductCategory.objects.filter(is_active=True),
#         'products': products_paginator,
#     }
#
#     return render(request, 'mainapp/products.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'title': product.name,
        'product': product,
    }
    return render(request, 'mainapp/product.html', context)
