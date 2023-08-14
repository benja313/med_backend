from rest_framework import serializers

from .models import Multimedia


class MultimediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Multimedia
        fields = ('multimedia_id', 'multimedia_path', 'multimedia_type')
