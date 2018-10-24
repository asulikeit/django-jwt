'''
Created on 2018. 10. 23.

@author: asulikeit
'''
from django.contrib.auth.base_user import BaseUserManager
from django.db import transaction


class UserManager(BaseUserManager):
 
    def create_user(self, username, password=None, **extra_fields):
        with transaction.atomic():
            user = self.model(username=username, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, username, password, **extra_fields):
        with transaction.atomic():
            extra_fields.setdefault('is_superuser', True)
            user = self.model(username=username, address='test', **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        