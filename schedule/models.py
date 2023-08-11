from django.db import models
from institution.models import Institutions

# Create your models here.
class Schedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    schedule_day = models.IntegerField()
    schedule_institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='schedule_institution')
    schedule_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schedules'
