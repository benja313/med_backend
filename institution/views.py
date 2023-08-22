from rest_framework import viewsets
from .serializer import InstitutionsSerializer
from .models import Institutions

# Create your views here.


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institutions.objects.all()
    serializer_class = InstitutionsSerializer
