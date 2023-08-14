from django.db import models

class TypeMultimedia(models.Model):
    type_multi_id = models.IntegerField(primary_key=True)
    type_multi_name = models.CharField(max_length=45)
    type_multi_description = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'type_multimedia'