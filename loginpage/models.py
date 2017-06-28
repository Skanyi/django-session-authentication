from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have a valid email address")

        if not kwargs.get('username'):
            raise ValueError("User must have a username")

        account = self.model(
            email=self.normalize_email(email),
            username=kwargs.get("username"),
            firstname=kwargs.get("firstname"),
            lastname=kwargs.get("lastname"),
        )

        account.set_password(password)
        account.save()

        return Account

    def create_superuser(self, email, password=None, **kwargs):
        account = self.create_user(email, password, kwargs)

        account.is_admin = True
        acoount.save()

        return account


class Account(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)

    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)

    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
