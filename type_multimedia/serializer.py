from rest_framework import serializers

from .models import TypeMultimedia


class TypeMultimediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeMultimedia
        fields = ('type_multi_id', 'type_multi_name',  'type_multi_description')