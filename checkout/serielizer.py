from rest_framework import serializers

from .models import Checkouts


class CheckoutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkouts
        fields = ('checkout_id', 'checkout_observation', 'checkout_code_transaction', 'checkout_token', 'checkout_authorization_code',
                  'checkout_payment_type_code', 'checkout_buy_order', 'checkout_vci', 'checkout_card_detail')
