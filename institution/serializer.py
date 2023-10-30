from rest_framework import serializers

from user.serializer import UserSerializer

from .models import Institutions


class InstitutionsSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Institutions
        fields = '__all__'
