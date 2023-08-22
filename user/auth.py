from django.contrib.auth import login
from django.contrib.auth.hashers import get_hasher
from django.utils.crypto import get_random_string
from rest_framework import serializers
from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#from .serializer import UserCreateSerializer
from django.contrib.auth.models import BaseUserManager

UserModel = get_user_model()

class BaseUserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        print(extra_fields, email, password, username)
        if not username:
            raise ValueError("The given username must be set")
        email = normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = UserModel
        username = GlobalUserModel.normalize_username(username)

        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, email, password, **extra_fields)

def authenticate(email=None, password=None, **kwargs):
    if email is None:
        username = kwargs.get(UserModel.EMAIL_FIELD)
    if email is None or password is None:
        return
    try:
        print('esta en try')
        user = UserModel.objects.get(email=email)
        print(user)
    except UserModel.DoesNotExist:
        # Run the default password hasher once to reduce the timing
        print('entra en password')
        # difference between an existing and a nonexistent user (#20760).
        UserModel().set_password(password)
    else:
        print('entra en else final')
        if user.check_password(password):
            return user



def make_password(password, salt=None, hasher="default"):
    """
    Turn a plain-text password into a hash for database storage

    Same as encode() but generate a new random salt. If password is None then
    return a concatenation of UNUSABLE_PASSWORD_PREFIX and a random string,
    which disallows logins. Additional random string reduces chances of gaining
    access to staff or superuser accounts. See ticket #20079 for more info.
    """
    UNUSABLE_PASSWORD_PREFIX = "!"  # This will never be a valid encoded hash
    UNUSABLE_PASSWORD_SUFFIX_LENGTH = (
        40  # number of random chars to add after UNUSABLE_PASSWORD_PREFIX
    )

    if password is None:
        return UNUSABLE_PASSWORD_PREFIX + get_random_string(
            UNUSABLE_PASSWORD_SUFFIX_LENGTH
        )
    if not isinstance(password, (bytes, str)):
        raise TypeError(
            "Password must be a string or bytes, got %s." % type(password).__qualname__
        )
    hasher = get_hasher(hasher)
    salt = salt or hasher.salt()
    return hasher.encode(password, salt)


def normalize_email(email):
    """
    Normalize the email address by lowercasing the domain part of it.
    """
    email = email or ""
    try:
        email_name, domain_part = email.strip().rsplit("@", 1)
    except ValueError:
        pass
    else:
        email = email_name + "@" + domain_part.lower()
    return email
