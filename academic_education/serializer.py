from rest_framework import serializers

from .models import AcademicEducation


class AcademicEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicEducation
        fields = ('academic_education_id', 'academic_education_name', 'academic_education_city', 'academic_education_country', 'academic_education_professional')
