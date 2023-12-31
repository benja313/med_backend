from rest_framework import serializers

from .models import Specialties
from user.serializer import UserSerializer, UserInstitutionsSerializer


class SpecialtiesSerializer(serializers.ModelSerializer):
    #users = UserSerializer(many=True)

    class Meta:
        model = Specialties
        fields = '__all__'

class SpecialtiesUsersSerializer(serializers.ModelSerializer):
        users = UserInstitutionsSerializer(many=True, read_only=True)

        class Meta:
            model = Specialties
            fields = '__all__'