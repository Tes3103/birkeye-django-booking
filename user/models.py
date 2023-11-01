from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_active=True, is_admin=False, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is reuired')
        user = self.model(
            email=self.normalize_email(email), **extra_fields
        )
        user.set_password(password)
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            is_admin=True,
            **extra_fields

        )

        return user


class User(AbstractBaseUser):
    """Define a custom User Model"""
    email = models.EmailField(verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'name', 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def is_admin(self):
        """Return User Admin state"""
        return self.admin

    @property
    def is_superuser(self):
        """Return User Superuser state"""
        return self.admin

    @property
    def is_active(self):
        """Return User Active state"""
        return self.active

    def __str__(self):
        """Override str method"""
        return self.email
