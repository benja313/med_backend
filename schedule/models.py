from django.db import models
from institution.models import Institutions
from user.models import Users

# Create your models here.


class Schedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    schedule_day = models.IntegerField()
    institution_id = models.ForeignKey(
        Institutions, models.DO_NOTHING, db_column='institution_id')
    professional_id = models.ForeignKey(
        Users, models.DO_NOTHING, db_column='professional_id')
    schedule_status = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'schedules'
