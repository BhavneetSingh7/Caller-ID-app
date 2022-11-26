"""
Custom User Model for Phone number authentication
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    Manager of our Custom User Model. 
    Handles creating client users and admin users
    """
    def create_user(self, phone_number, name, password, **extra_fields):
        if not phone_number:
            raise ValueError('No phone number provided')
        if not name:
            raise ValueError('No Name provided')
        user = self.model(phone_number=phone_number, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, name, password, **extra_fields):
        if not phone_number:
            raise ValueError('No phone number provided')
        if not name:
            raise ValueError('No Name provided')
        user = self.create_user(phone_number, name, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User with phone number as unique auth field
    Accounts for Registered users are made in this model
    """
    #Some countries have 13 digits phone number plus max 4 digits for Country code
    # Dash or space separating numbers e.g. +123-4679733483
    phone_number = models.CharField(max_length=18, unique=True, blank=False)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=30, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number' #login using Phone number
    REQUIRED_FIELDS = ['name']

    objects = UserManager() # Responsible for creating users
