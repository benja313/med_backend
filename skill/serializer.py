from rest_framework import serializers

from .models import Skills


class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ('skill_id', 'skill_name', 'skill_description')