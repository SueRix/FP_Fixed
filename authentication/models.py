from django.db import models
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(models.Model):
    email = models.EmailField(
        max_length=40,
        unique=True,
    )
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
