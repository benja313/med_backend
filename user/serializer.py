from django.contrib.auth import login
from rest_framework import serializers

from .models import Users, AuthUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
        'id', 'username', 'email', 'user_rut', 'user_dv', 'user_phone', 'password', 'user_lastname',
        'user_avatar', 'user_delete',
        'user_token_login', 'user_token_reset', 'user_nationality', 'user_profession_id', 'user_birthdate',
        'user_insurance', 'user_num_sis')


class UserRegisterationSerializer(serializers.ModelSerializer):
    # Serializer class to serialize registration requests and create a new user.

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create(self, validated_data):
        return self.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to authenticate users with email and password.
    """
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        diccionario = dict(data)  # Convertir la cadena en un diccionario
        email = diccionario['email']
        password = diccionario['password']
        user = UserLoginSerializer.authenticate(email=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

    def authenticate(email=None, password=None, **kwargs):
        print('entra en autenticacio')
        UserModel = get_user_model()

        if email is None:
            print('email es none')
            username = kwargs.get(UserModel.EMAIL_FIELD)
        if email is None or password is None:
            print('no llega el mail o password')
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

class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
        'id', 'username', 'email', 'password', 'phone')
