from rest_framework import serializers

from .models import Insurances


class InsurancesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurances
        fields = ('insurance_id', 'insurance_name', 'insurance_description', 'insurances_type')
        