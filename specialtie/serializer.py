from rest_framework import serializers

from .models import Specialties


class SpecialtiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Specialties
        fields = ('specialty_id', 'specialty_name', 'specialty_description')
