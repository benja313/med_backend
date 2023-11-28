from rest_framework import serializers
from institution.serializer import InstitutionsSerializer
from .models import Services


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class ServicesInstitutionSerializer(serializers.ModelSerializer):
    service_institution_id = InstitutionsSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        # fields = ('service_id', 'servicio_break', 'service_weeks_enable', 'service_institution', 'service_price')
        fields = '__all__'