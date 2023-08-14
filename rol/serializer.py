from rest_framework import serializers

from .models import Roles


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = ('role_id', 'rol_name', 'rol_description', 'rol_delete')

    