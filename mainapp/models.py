from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True, null=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='имя', max_length=128, unique=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    description = models.TextField(verbose_name='описание продукта', blank=True, null=True)
    image_url = models.ImageField(upload_to='products_images', blank=True, verbose_name='изображение')
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на сладе', default=0)
    is_active = models.BooleanField(verbose_name='активен', default=True)

    def __str__(self):
        return f'{self.name} | {self.category}'
