from rest_framework import serializers

from .models import Specialties


class SpecialtiesSerializer(serializers.ModelSerializer):
    # users = UserSerializer(many=True)

    class Meta:
        model = Specialties
        fields = '__all__'