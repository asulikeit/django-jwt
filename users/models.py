from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .domains import UserManager


class User(AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(max_length=99, unique=True)
    email = models.EmailField(max_length=99)
    address = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    class Meta:
        db_table = "tmp_users"
    