from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    DB_CHOICES = (('MS', 'Microsoft SQL'), ('OS', 'Oracle SQL'), ('PG', 'PostgreSQL'),)

    username = None
    email = models.EmailField(_('email address'), unique=True)
    database = models.CharField(max_length=2, choices=DB_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
