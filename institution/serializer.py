from rest_framework import serializers

from .models import Institutions


class InstitutionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institutions
        fields = '__all__'
