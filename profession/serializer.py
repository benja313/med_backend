from rest_framework import serializers

from .models import Professions


class ProfessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professions
        fields = ('profession_id', 'profesion_name', 'profesion_description')
