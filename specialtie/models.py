from django.db import models
from user.models import Users

# Create your models here.
class Specialties(models.Model):
    specialty_id = models.AutoField(primary_key=True)
    specialty_name = models.CharField(max_length=45)
    specialty_description = models.CharField(max_length=45)
    users = models.ManyToManyField(Users, related_name='specialties')

    class Meta:
        managed = False
        db_table = 'specialties'