from django.db import models
from type_insurance.models import TypeInsurances

# Create your models here.
class Insurances(models.Model):
    insurance_id = models.IntegerField(primary_key=True)
    insurance_name = models.CharField(max_length=45)
    insurance_description = models.CharField(max_length=45)
    insurances_type = models.ForeignKey(TypeInsurances, models.CASCADE)

    class Meta:
        managed = False
        db_table = 'insurances'