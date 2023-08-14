from django.db import models

# Create your models here.
class TypeInsurances(models.Model):
    type_insurance_id = models.IntegerField(primary_key=True)
    type_insurance_name = models.CharField(max_length=45)
    type_insurance_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'type_insurances'