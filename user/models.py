from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', null=True, blank=True)
    avatar = models.ImageField(upload_to='user/', verbose_name='аватар', null=True, blank=True)
    country = models.CharField(max_length=150, verbose_name='страна', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []