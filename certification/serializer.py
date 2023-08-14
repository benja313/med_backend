from rest_framework import serializers

from .models import Certifications


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = ('certificaion_id', 'certification_name', 'certification_path', 'certificacion_institution')
