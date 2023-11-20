from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from .models import Specialties, Users
from .serializer import SpecialtiesSerializer, SpecialtiesUsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
# Create your views here.


class SpecialtiesViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Specialties.objects.all()
    serializer_class = SpecialtiesSerializer
    lookup_field = 'specialty_id'

    def perform_create(self, request):
        try:

            # Obtenemos la lista de usuarios de la solicitud
            users = self.request.data.get('users', [])

            serializer = SpecialtiesSerializer(data=request.data)

            # Verificar si los datos del serializador son válidos
            if serializer.is_valid():

                instance = serializer.save()
                # Establecer la relación Many-to-Many con los usuarios
                instance.users.set(users)

                specialties = Specialties.objects.filter(users=users[0])
                serializerGet = SpecialtiesSerializer(specialties, many=True)
                return Response(serializerGet.data, status=status.HTTP_201_CREATED)
            else:
                # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Specialties.DoesNotExist:
            # Capturamos una excepción si el objeto no existe en la base de datos
            return Response({"error": "El objeto no existe."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            return Response({"error": e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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

@api_view(['POST'])
def searchSpecialties(request):
    #queryset = super().get_queryset()
    query = request.data['keyword']
    if query:
        specialties = Specialties.objects.filter(specialty_name__icontains=query)
        serializer = SpecialtiesSerializer(specialties, many=True)

        # return Response(serializer.data, status=status.HTTP_200_OK)
        #qs_json = serializers.serialize('json', estaciones)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #return Response(specialties, status=status.HTTP_200_OK)

    return Response([],status=status.HTTP_200_OK)

@api_view(['GET'])
def get_specialties_users(request, id):
        user_id = id
        # direccion
        # nombre
        # profesion
        # horarios

        #specialties = Specialties.objects.filter(specialty_id=id)
        specialties = Specialties.objects.prefetch_related('users', 'users__institutions').all()
        # 'users__institutions'

        print(specialties)

        serializer = SpecialtiesUsersSerializer(specialties, many=True)

        return Response(serializer.data)
