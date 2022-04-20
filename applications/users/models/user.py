from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, email, passwd=None):
        if not email:
            raise ValueError("El cliente debe tener un email.")
        user = self.model(
            email=email,
            passwd=passwd
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, email, passwd):
        user = self.create_user(
            email = email, 
            password = passwd
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Representation of a User
    """
    id     = models.BigAutoField(primary_key=True)
    passwd = models.CharField('Passwd', max_length=256)
    name   = models.CharField('Name', max_length=50)
    email  = models.EmailField('Email', max_length=100, unique=True)

    objects        = UserManager()
    USERNAME_FIELD = 'email'
