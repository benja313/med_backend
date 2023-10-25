from rest_framework import viewsets
from .serializer import InstitutionsSerializer
from .models import Institutions
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
        # Crea la institución y agrega el usuario actual
        institutions = serializer.save()
        institutions.users.add(self.request.user)

    def get_queryset(self, request, pk=None):
        # Obtener las instituciones del usuario especificado en el parámetro
        user_id = self.kwargs['pk']
        institutions = Institutions.objects.filter(id=user_id)
        serializer = InstitutionsSerializer(institutions, many=True)
        return Response(serializer.data)
