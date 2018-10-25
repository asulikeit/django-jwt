from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, BaseUserManager
)
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
#         with transaction.atomic():
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
#         with transaction.atomic():
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.model(username=username, address='test', **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(max_length=99, db_index=True, unique=True)
    email = models.EmailField(max_length=99)
    address = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    class Meta:
        db_table = "tmp_users"
        
    def __str__(self):
        return self.username
    
