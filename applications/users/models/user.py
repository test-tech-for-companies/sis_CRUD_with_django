from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extrafields):
        if not email:
            raise ValueError("El cliente debe tener un email.")
        user = self.model(
            email=self.normalize_email(email),
            password=password,
            **extrafields            
        )
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email = email, 
            password = password
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Representation of a User
    """
    id     = models.BigAutoField(primary_key=True)
    password = models.CharField('Password', max_length=256)
    name   = models.CharField('Name', max_length=50)
    email  = models.EmailField('Email', max_length=100, unique=True)

    objects        = UserManager()
    USERNAME_FIELD = 'email'
