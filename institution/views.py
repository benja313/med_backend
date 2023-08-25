from rest_framework import viewsets
from .serializer import InstitutionsSerializer
from .models import Institutions
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class InstitutionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Institutions.objects.all()
    serializer_class = InstitutionsSerializer
