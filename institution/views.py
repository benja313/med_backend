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
    lookup_field = 'institution_id'

    def perform_create(self, request):
        try:
            # Obtenemos la lista de usuarios de la solicitud
            users = self.request.data.get('users', [])

            serializer = InstitutionsSerializer(data=request.data)
            # Verificar si los datos del serializador son válidos
            if serializer.is_valid():
                # Guardar la institución
                instance = serializer.save()
                # Establecer la relación Many-to-Many con los usuarios
                instance.users.set(users)

                institutions = Institutions.objects.filter(users=users[0])
                serializerGet = InstitutionsSerializer(institutions, many=True)
                return Response(serializerGet.data, status=status.HTTP_201_CREATED)
            else:
                # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Institutions.DoesNotExist:
            # Capturamos una excepción si el objeto no existe en la base de datos
            return Response({"error": "El objeto no existe."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_institutions_users(self, request, pk=None):
        # Obtener las instituciones del usuario especificado en el parámetro
        user_id = self.kwargs['pk']
        institutions = Institutions.objects.filter(users=user_id)
        serializer = InstitutionsSerializer(institutions, many=True)
        return Response(serializer.data)

    def delete_user_institution(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = int(kwargs.get('user_id'))

        # Verificar si el usuario existe en la institución
        if instance.users.filter(pk=user_id).exists():
            instance.users.remove(user_id)
            instance.save()

            institutions = Institutions.objects.filter(users=user_id)
            serializer = InstitutionsSerializer(institutions, many=True)
            return Response({"detail": "La relación entre la institución y el usuario ha sido eliminada.", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "La relación entre la institución y el usuario no existe."}, status=status.HTTP_404_NOT_FOUND)

    def perform_link(self, request):
        try:
            institution_id = request.data.get('institution_id')
            user_id = request.data.get('user_id')

            print(institution_id)
            print(user_id)
            # Busca la institución por el ID proporcionado
            institution = Institutions.objects.get(
                institution_id=institution_id)
            print(institution)
            user = Users.objects.get(id=user_id)
            print(user)
            # Añade el usuario a la relación muchos a muchos con la institución
            institution.users.add(user)

            institutions = Institutions.objects.filter(users=user_id)
            serializer = InstitutionsSerializer(institutions, many=True)
            return Response({"detail": "Usuario vinculado a la institución correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            print(e)
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
