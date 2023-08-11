from django.db import models

class Profesionals(models.Model):
    profesional_id = models.AutoField(primary_key=True)
    profesional_name = models.CharField(max_length=45)
    profesional_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'profesionals'