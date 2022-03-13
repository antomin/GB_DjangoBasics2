import hashlib
import random
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


def activation_key_generator(email):
    pass


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True

    # def activation_key_generator(self):
    #     salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
    #     activation_key = hashlib.sha1(str(self.email + salt).encode('utf8')).hexdigest()
    #     return activation_key
