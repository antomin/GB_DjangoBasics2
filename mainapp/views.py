from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, TemplateView

from mainapp.models import Product, ProductCategory


class Index(TemplateView):
    template_name = 'mainapp/index.html'
    extra_context = {'title': 'главная'}


def products(request, pk=None, page=1):
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products_list = Product.objects.filter(is_active=True)
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        products_list = Product.objects.filter(is_active=True, category__pk=pk)

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
        'object_list': products_paginator,
        'category': category
    }

    return render(request, 'mainapp/products.html', context)

# TODO AJAX
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
#     return render(request, 'mainapp/product_list.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'mainapp/product.html'
    extra_context = {'title': 'продукт'}
