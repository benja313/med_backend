from rest_framework import serializers

from .models import Services


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('service_id', 'servicio_break', 'service_weeks_enable', 'service_institution', 'service_price')
        