from rest_framework import serializers

from .models import Institutions


class InstitutionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institutions
        fields = ('institution_id', 'institution_name', 'institution_mail','institution_phone', 'institution_state_id', 'institution_city_id', 'institution_street', 'institution_lat', 'institution_lon', 'institution_user')
