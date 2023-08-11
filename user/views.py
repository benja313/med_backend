#from typing import re

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
# Importar el modelo
from django.http import JsonResponse, HttpResponse
from requests import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
import json
from .models import Users

# Create your viewss here.
@api_view(['GET'])
def index(request):
    serializer_context = {
        'request': Request(request),
    }
    users = Users.objects.all()
    #estaciones = EstacionModel.objects.select_related('volcan')
    serializer = UserSerializer(users, many=True)

    #return Response(serializer.data, status=status.HTTP_200_OK)
    #qs_json = serializers.serialize('json', users)
    return Response(serializer.data, status=status.HTTP_200_OK)