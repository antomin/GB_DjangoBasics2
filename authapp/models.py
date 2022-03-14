from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='аватар', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires + timedelta(hours=48):
            return False
        return True


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMAIL = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMAIL, 'Ж'),
    )

    user = models.OneToOneField(ShopUser, unique=True, db_index=True, on_delete=models.CASCADE)
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.CharField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)


@receiver(post_save, sender=ShopUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShopUserProfile.objects.create(user=instance)


@receiver(post_save, sender=ShopUser)
def save_user_profile(sender, instance, **kwargs):
    instance.shopuserprofile.save()



