from rest_framework import viewsets, status
from .serializer import ServicesSerializer, ServicesInstitutionSerializer
from .models import Services
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
# Create your views here.


class ServiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    lookup_field = 'service_id'

    def perform_create(self, request):
        try:
            # Obtenemos la lista de usuarios de la solicitud
            institution_id = self.request.data.get('institution_id')
            serializer = ServicesSerializer(data=request.data)
            # Verificar si los datos del serializador son válidos
            if serializer.is_valid():
                # Guardar la institución
                serializer.save()

                services = Services.objects.filter(institution_id=institution_id)
                serializerGet = ServicesInstitutionSerializer(services, many=True)
                return Response(serializerGet.data, status=status.HTTP_201_CREATED)
            else:
                # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Services.DoesNotExist:
            # Capturamos una excepción si el objeto no existe en la base de datos
            return Response({"error": "El objeto no existe."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_services_institutions(self, request, pk=None):
        # Obtener las instituciones del usuario especificado en el parámetro
        institution_id = self.kwargs['pk']
        service = Services.objects.filter(service_institution_id=institution_id)
        serializer = ServicesSerializer(service, many=True)
        return Response(serializer.data)

    def delete_service(self, request, *args, **kwargs):

        id = int(kwargs.get('service_id'))
        institution_id = int(kwargs.get('service_institution_id'))
        estacion = Services.objects.get(service_id=id)
        estacion.delete()

        # Verificar si el usuario existe en la institución
        if estacion.exists():
            estacion.delete()
            services = Services.objects.filter(service_institution=institution_id)
            serializer = ServicesSerializer(services, many=True)
            return Response({"detail": "El ítem eliminado.", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "El ítem no existe."}, status=status.HTTP_404_NOT_FOUND)


