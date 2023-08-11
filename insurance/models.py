from django.db import models

# Create your models here.
class Insurances(models.Model):
    insurance = models.OneToOneField('TypeInsurances', models.DO_NOTHING, primary_key=True)
    insurance_name = models.CharField(max_length=45)
    insurance_description = models.CharField(max_length=45)
    insurances_type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'insurances'