from django.db import models

# Create your models here.
class Specialties(models.Model):
    specialty_id = models.IntegerField(primary_key=True)
    specialty_name = models.CharField(max_length=45)
    specialty_description = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialties'