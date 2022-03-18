from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created_ad = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    updated_ad = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def item_sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        all_baskets = Basket.objects.filter(user=self.user)
        return sum(basket.item_sum() for basket in all_baskets)

    def total_quantity(self):
        all_baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in all_baskets)

    # def get_items(self):
    #     return self.objects.filter(user=self.user)
