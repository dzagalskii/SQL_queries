from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=16)
    email = models.EmailField(_('email address'), unique=True)
    data_schemas = models.CharField(max_length=16)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
