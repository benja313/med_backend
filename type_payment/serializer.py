from rest_framework import serializers

from .models import TypePayment


class TypePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypePayment
        fields = ('type_payment_id', 'type_payment_name')