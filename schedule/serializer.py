from rest_framework import serializers

from .models import Schedules


class SchedulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedules
        fields = ('schedule_id', 'schedule_start', 'schedule_end', 'schedule_day', 'schedule_institution', 'schedule_status')