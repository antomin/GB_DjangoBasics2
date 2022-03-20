from django.conf import settings
from django.db import models
from django.shortcuts import get_object_or_404

from mainapp.models import Product


class BasketQuerySet(models.QuerySet):
    def delete(self):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super(BasketQuerySet, self).delete()


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
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

    @staticmethod
    def get_item(pk):
        return get_object_or_404(Basket, pk=pk)

    def delete(self, using=None, keep_parents=False):
        self.product.quantity += self.quantity
        self.product.save()
        super(Basket, self).delete()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk:
            self.product.quantity -= self.quantity - Basket.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(Basket, self).save()


