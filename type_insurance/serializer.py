from rest_framework import serializers

from .models import TypeInsurances


class TypeInsurancesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeInsurances
        fields = ('type_insurance_id', 'type_insurance_name', 'type_insurance_description')
