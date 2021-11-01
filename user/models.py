from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    data_schemas = models.CharField(max_length=16)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
