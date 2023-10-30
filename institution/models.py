from django.db import models
from user.models import Users

# Create your models here.


class Institutions(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=100)
    institution_mail = models.EmailField(max_length=45, blank=True, null=True)
    institution_phone = models.CharField(max_length=15, blank=True, null=True)
    institution_state_id = models.IntegerField(blank=True, null=True)
    institution_city_id = models.IntegerField(blank=True, null=True)
    institution_street = models.CharField(
        max_length=100, blank=True, null=True)
    institution_lat = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    institution_lon = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    users = models.ManyToManyField(Users, related_name='institutions')

    class Meta:
        managed = False
        db_table = 'institutions'
