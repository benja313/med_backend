from django.db import models

# Create your models here.
class Professions(models.Model):
    profession_id = models.IntegerField(primary_key=True)
    profesion_name = models.CharField(max_length=45)
    profesion_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'professions'