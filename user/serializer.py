from rest_framework import serializers

from .models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('user_id', 'user_name', 'user_email', 'user_rut', 'user_dv','user_phone', 'user_password', 'user_lastname', 'user_avatar', 'user_delete',
                'user_token_login', 'user_token_reset', 'user_nationality', 'user_profession_id', 'user_birthdate', 'user_insurance', 'user_num_sis')