from django.db import models

# Create your models here.
class Checkouts(models.Model):
    checkout_id = models.IntegerField(primary_key=True)
    checkout_observation = models.CharField(max_length=45)
    checkout_code_transaction = models.CharField(max_length=45)
    checkout_token = models.CharField(max_length=45, blank=True, null=True)
    checkout_authorization_code = models.CharField(max_length=45, blank=True, null=True)
    checkout_payment_type_code = models.CharField(max_length=45, blank=True, null=True)
    checkout_buy_order = models.CharField(max_length=45, blank=True, null=True)
    checkout_vci = models.CharField(max_length=45, blank=True, null=True)
    checkout_card_detail = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkouts'