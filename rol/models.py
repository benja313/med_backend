from django.db import models

# Create your models here.
class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    rol_name = models.CharField(max_length=45)
    rol_description = models.CharField(max_length=45)
    rol_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'