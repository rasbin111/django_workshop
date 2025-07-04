from django.db import models
from datetime import datetime

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,

)

from django.utils import timezone
from django.utils.text import slugify

# from django.utils.translation import ugettext_lazy as _


def avatar_directory_path(instance, filename):  # pylint: disable = unused-argument
    """Upload path to save file"""
    return f"user_account/{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}_{filename}"


def get_unique_username(model_instance, full_name, slug_field_name):
    """
    Takes a model instance, sluggable field name (such as 'title') of that
    model as string, slug field name (such as 'slug') of the model as string;
    returns a unique slug as string.
    """
    # pylint: disable = protected-access
    slug = slugify(full_name)
    unique_slug = slug
    extension = 1
    model_class = model_instance.__class__

    while model_class._default_manager.filter(
        **{slug_field_name: unique_slug}
    ).exists():
        unique_slug = f"{slug}-{extension}"
        extension += 1
    return unique_slug


class UserManager(BaseUserManager):
    """
    Custom user manager for creating and managing user instances.

    This class provides methods for creating regular users and superusers.
    It extends thefunctionality of the base user manager
    provided by Django's authentication framework.

    Args:
        BaseUserManager (class): Base user manager class provided by Django.

    Methods:
        _create_user(email, password, is_staff, is_superuser, **extra_fields):
            Creates and saves a new user instance with the given email, password, and
            additional fields.
        create_user(email, password, **extra_fields):
            Creates and saves a new regular user instance with the given email,
            password, and additional fields.
        create_superuser(email, password, **extra_fields):
            Creates and saves a new superuser instance with the given email,
            password, andadditional fields.
    """

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        """Function that calls create_user func"""
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Function that calls _create_user func to create superuser"""
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Model => User"""

    GENDER_CHOICES = ((0, "Male"), (1, "Female"), (2, "Other"))
    USER_TYPES = (
        ("manager", "Manager"),
        ("operation-manager", "Operation Manager"),
    )
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, null=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=avatar_directory_path, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPES, default="manager")
    password_reset = models.BooleanField(default=False)
    timezone = models.CharField(max_length=100, default="Asia/Kathmandu")
    is_email_verified = models.BooleanField(default=False)
    created_by_self = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_email(self):
        """returns user email"""
        return self.email

    @property
    def get_gender_name(self):
        return self.get_gender_display()

    def save(self, *args, **kwargs):
        """Post save method after triggering User model"""
        self.email = self.email.lower()
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        if not self.username:
            self.username = get_unique_username(
                self, self.first_name + " " + self.last_name, "username"
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username
