from django.db import models
from institution.models import Institutions

class Services(models.Model):
    service_id = models.IntegerField(primary_key=True)
    servicio_break = models.IntegerField()
    service_weeks_enable = models.IntegerField()
    service_institution = models.ForeignKey(Institutions, models.DO_NOTHING, blank=True, null=True)
    service_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'services'