from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Schedules
from .serializer import SchedulesSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ScheduleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer
    lookup_field = 'schedule_id'

    def perform_update(self, request, *args, **kwargs):

        try:
            user_id = int(kwargs.get('schedule_professional_id'))

            schedules_data = request.data

            schedules_data_temp = list(
                map(lambda x: {**x, 'professional_id': user_id}, schedules_data))

        # Eliminar registros anteriores del usuario
            Schedules.objects.filter(professional_id=user_id).delete()

            serializer = SchedulesSerializer(
                data=schedules_data_temp, many=True)

            # Verificar si los datos del serializador son válidos
            if serializer.is_valid():
                # Guardar la institución
                serializer.save()

                # get
                schedules = Schedules.objects.filter(professional_id=user_id)
                serializerGet = SchedulesSerializer(schedules, many=True)

                return Response(serializerGet.data, status=status.HTTP_201_CREATED)
            else:
                # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Schedules.DoesNotExist:
            # Capturamos una excepción si el objeto no existe en la base de datos
            return Response({"error": "El objeto no existe."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            print(e)
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_schedules_users(self, request, pk=None):
        user_id = self.kwargs['pk']
        schedules = Schedules.objects.filter(professional_id=user_id)
        serializerGet = SchedulesSerializer(schedules, many=True)

        return Response(serializerGet.data, status=status.HTTP_201_CREATED)

    # end def
