from django.db import models

# Create your models here.
class Skills(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=45)
    skill_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'skills'