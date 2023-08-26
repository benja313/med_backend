from django.db import models
from django.contrib.auth.models import User
from insurance.models import Insurances
from profession.models import Professions


class Users(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    # username = models.CharField(unique=True, max_length=150, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    rut = models.IntegerField(blank=True, null=True)
    dv = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)
    avatar = models.CharField(blank=True, null=True)
    mother_last_name = models.CharField(blank=True, null=True)
    token_login = models.CharField(blank=True, null=True)
    token_reset = models.CharField(blank=True, null=True)
    nacionality = models.CharField(blank=True, null=True)
    profession = models.ForeignKey(
        Professions, models.DO_NOTHING, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    insurance = models.ForeignKey(
        Insurances, models.DO_NOTHING, blank=True, null=True)
    num_sis = models.IntegerField(blank=True, null=True)

    # objects = CustomUserManager()
    class Meta:
        managed = False
        db_table = 'auth_user'
