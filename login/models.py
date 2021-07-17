from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, uid, username, password=None):

        if not uid:
            raise ValueError('must have user uid')
        if not username:
            raise ValueError('must have user username')

        user = self.model(
            uid=uid,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, uid, username, password=None):

        user = self.create_user(
            uid=uid,
            username = username,
            password = password

        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    uid = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.uid

    @property
    def is_staff(self):
        return self.is_admin