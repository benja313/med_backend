from rest_framework import serializers

from .models import Locks


class LocksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Locks
        fields = ('lock_id', 'lock_date_start', 'lock_date_end', 'lock_user')
        