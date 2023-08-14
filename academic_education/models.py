from django.db import models
from user.models import Users

# Create your models here.
class AcademicEducation(models.Model):
    academic_education_id = models.IntegerField(primary_key=True)
    academic_education_name = models.CharField(max_length=45)
    academic_education_city = models.CharField(max_length=45, blank=True, null=True)
    academic_education_country = models.CharField(max_length=45, blank=True, null=True)
    academic_education_professional = models.ForeignKey(Users, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_education'