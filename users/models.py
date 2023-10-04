from django.contrib.auth.models import AbstractUser
from django.db import models

from shelter.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.CharField(verbose_name='email', unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    phone = models.CharField(verbose_name='телефон', max_length=35, **NULLABLE)
    telegram = models.CharField(verbose_name='телеграм ник', max_length=50, **NULLABLE)
    avatar = models.ImageField(verbose_name='аватар', upload_to='users/', **NULLABLE)
