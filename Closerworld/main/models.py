from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True, max_length=200, null=False, blank=False)
    age = models.IntegerField()
    class Gender(models.TextChoices):
        male = 'M', 'Male'
        female = 'F', 'Female'
        transgender = 'T', 'Transgender'
    gender = models.CharField(max_length= 2, choices=Gender.choices)
    phone = PhoneNumberField(null=False, blank=False)
    business = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email