#from typing import re

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from .serializer import UserSerializer, UserLoginSerializer, UserRegisterationSerializer, User2Serializer
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json
from .models import Users
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from specialtie.models import Specialties
# Create your viewss here.
@api_view(['GET'])
def index(request):
    try:
        serializer_context = {
            'request': Request(request),
        }
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)

def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        raise serializers.ValidationError("Incorrect Credentials")

def refreshToken(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    token = RefreshToken.for_user(user)
    data = UserRegisterationSerializer.data
    data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
    return Response(data, status=status.HTTP_200_OK)

User = get_user_model()

class UserRegisterationAPIView(GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserRegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        print(user.id, 'este es el id')
        serializer = User2Serializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getUsersByGroup(request, specialty):

    #estacions = User.objects.values('id_estacion', 'nombre').filter(volcan_id=id)
    group = Group.objects.get(id=1)
    users = group.user_set.all()
    specialties = Specialties.objects.filter(user__in=users)
    Specialties.objects.get(specialty_id=specialty)
    #specialty
    #usuarios = Group.objects.select_related('user')
    print(usuarios)

    return Response(users, status=status.HTTP_200_OK)