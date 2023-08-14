from rest_framework import serializers

from .models import Appointments


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ('appointment_id', 'appointment_patient', 'appointment_date_start', 'appointment_date_end', 'appointment_status', 'appointment_day', 'appointment_type_pay', 'appointment_service', 'appointment_first_time', 'appointment_checkout')
