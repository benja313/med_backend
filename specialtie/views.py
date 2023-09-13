from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from .models import Specialties
from .serializer import SpecialtiesSerializer
from rest_framework.response import Response
from rest_framework import status

class SpecialtieAPIView(APIView):
    def get(self, request):
        specialties = Specialties.objects.all()
        serializer = SpecialtiesSerializer(specialties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpecialtiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        specialtie = Specialties.objects.get(pk=pk)
        serializer = SpecialtiesSerializer(specialtie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        specialtie = Specialties.objects.get(pk=pk)
        specialtie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

