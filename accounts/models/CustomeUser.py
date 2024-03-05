from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
)
from accounts.models.CustomeUserManager import CustomeBaseUserManager


class CustomeUser(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(max_length=12, unique = True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = [phone, username]

    objects = CustomeBaseUserManager()

    def __str__(self):
        return self.username
