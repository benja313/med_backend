from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Skills
from .serializer import SkillsSerializer
from rest_framework.response import Response
from user.models import Users

# Create your views here.
class SkillsViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    lookup_field = 'skill_id'

    def perform_create(self, request):
        try:
            # Obtenemos la lista de usuarios de la solicitud
            users = self.request.data.get('users', [])

            serializer = SkillsSerializer(data=request.data)
            # Verificar si los datos del serializador son válidos
            if serializer.is_valid():
                instance = serializer.save()
                # Establecer la relación Many-to-Many con los usuarios
                instance.users.set(users)

                institutions = Skills.objects.filter(users=users[0])
                serializerGet = SkillsSerializer(institutions, many=True)
                return Response(serializerGet.data, status=status.HTTP_201_CREATED)
            else:
                # Si los datos no son válidos, devolver una respuesta de error con los detalles de la validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Skills.DoesNotExist:
            # Capturamos una excepción si el objeto no existe en la base de datos
            return Response({"error": "El objeto no existe."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_skills_users(self, request, pk=None):
        # Obtener las habilidades del usuario especificado en el parámetro
        user_id = self.kwargs['pk']
        skills = Skills.objects.filter(users=user_id)
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data)

    def delete_user_skill(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id = int(kwargs.get('user_id'))

        # Verificar si el usuario existe en la institución
        if instance.users.filter(pk=user_id).exists():
            instance.users.remove(user_id)
            instance.save()

            skills = Skills.objects.filter(users=user_id)
            serializer = SkillsSerializer(skills, many=True)
            return Response({"detail": "La relación entre la institución y el usuario ha sido eliminada.", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "La relación entre la institución y el usuario no existe."}, status=status.HTTP_404_NOT_FOUND)

    def perform_link(self, request):
        try:
            skill_id = request.data.get('skill_id')
            user_id = request.data.get('user_id')


            # Busca la habilidad por el ID proporcionado
            skill = Skills.objects.get(skill_id=skill_id)
            user = Users.objects.get(id=user_id)
            # Añade el usuario a la relación muchos a muchos con las habilidades
            skill.users.add(user)

            skills = Skills.objects.filter(users=user_id)
            serializer = SkillsSerializer(skills, many=True)
            return Response({"detail": "Usuario vinculado a la institución correctamente.", "data": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            # Puedes capturar otras excepciones y manejarlas de manera personalizada
            print(e)
            return Response({"error": "Ha ocurrido un error inesperado."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
