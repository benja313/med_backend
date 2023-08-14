from django.db import models

class TypePayment(models.Model):
    type_payment_id = models.IntegerField(primary_key=True)
    type_payment_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'type_payment'