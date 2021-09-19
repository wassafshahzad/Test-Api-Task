from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import ModelState
from django.utils.translation import ugettext_lazy as _
from rest_framework_api_key.models import AbstractAPIKey

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserApiKey(AbstractAPIKey):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="api_key"
    )