from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True
