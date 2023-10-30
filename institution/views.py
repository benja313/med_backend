from rest_framework import viewsets, status
from .serializer import InstitutionsSerializer
from .models import Institutions, Users
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
# Create your views here.


class InstitutionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Institutions.objects.all()
    serializer_class = InstitutionsSerializer

    def perform_create(self, serializer):
        # Obtenemos la lista de usuarios de la solicitud
        users = self.request.data.get('users', [])

        # Verificar si los datos del serializador son válidos
        if serializer.is_valid():
            # Guardar la institución
            instance = serializer.save()
            # Establecer la relación Many-to-Many con los usuarios
            instance.users.set(users)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self, request, pk=None):
        # Obtener las instituciones del usuario especificado en el parámetro
        user_id = self.kwargs['pk']
        institutions = Institutions.objects.filter(users=user_id)
        serializer = InstitutionsSerializer(institutions, many=True)
        return Response(serializer.data)
