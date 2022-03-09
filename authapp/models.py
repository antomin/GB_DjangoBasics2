from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
