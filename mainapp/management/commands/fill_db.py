import json

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


def load_json(file):
    with open(file, 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_json('mainapp/fixtures/001_categories.json')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = category['fields']
            new_category['pk'] = category['pk']
            ProductCategory(**new_category).save()

        products = load_json('mainapp/fixtures/002_products.json')
        Product.objects.all().delete()
        for product in products:
            new_product = product['fields']
            category = new_product['category']
            _category = ProductCategory.objects.get(id=category)
            new_product['category'] = _category
            Product(**new_product).save()

        ShopUser.objects.create_superuser('admin', 'admin@geekshop.local', 'admin', age=36)
