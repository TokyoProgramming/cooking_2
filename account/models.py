from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# (2)
class UserProfileManager(BaseUserManager):
    """ Manager for the user profile """

    def create_user(self, email, name, password=None):
        """ create a new user profile """
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # """ convert to hash {set_password} """
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# (1)
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # overwrite
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # def get_full_name(self):

    def __str__(self):
        return self.email
