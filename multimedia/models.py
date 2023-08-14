from django.db import models
from type_multimedia.models import TypeMultimedia

# Create your models here.
class Multimedia(models.Model):
    multimedia_id = models.IntegerField(primary_key=True)
    multimedia_path = models.CharField(max_length=45)
    multimedia_type = models.ForeignKey(TypeMultimedia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'multimedia'