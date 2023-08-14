from rest_framework import serializers

from .models import Profesionals


class ProfesionalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profesionals
        fields = ('profesional_id', 'profesional_name', 'profesional_description')
        