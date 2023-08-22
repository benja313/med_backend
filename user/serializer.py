from django.contrib.auth import login
from rest_framework import serializers

from . import auth
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


    def create(self, validated_data):
        return auth.create_user(**validated_data)


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
        user = auth.authenticate(email=email, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")



class User2Serializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = (
        'id', 'username', 'email', 'password', 'phone')
