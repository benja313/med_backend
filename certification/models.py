from django.db import models

# Create your models here.
class Certifications(models.Model):
    certificaion_id = models.IntegerField(primary_key=True)
    certification_name = models.CharField(max_length=45)
    certification_path = models.CharField(max_length=45, blank=True, null=True)
    certificacion_institution = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'certifications'