from django.db import models
from user.models import Users

# Create your models here.
class Locks(models.Model):
    lock_id = models.IntegerField(primary_key=True)
    lock_date_start = models.DateTimeField()
    lock_date_end = models.DateTimeField()
    lock_user = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'locks'