from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra):
        user = self.model(
            username=username,
            **extra
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)

        if extra.get("is_staff") is not True:
            raise ValueError('Please set is_staff=True')
        if extra.get("is_superuser") is not True:
            raise ValueError('Please set is_superuser=True')

        return self.create_user(username=username, password=password, **extra)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class FollowModel(models.Model):
    follow_from = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower')
    follow_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    class Meta:
        unique_together = ('follow_from', 'follow_to')
