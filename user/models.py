from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    user_rut = models.IntegerField()
    user_dv = models.CharField(max_length=45)
    user_phone = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    user_lastname = models.CharField(max_length=45)
    user_mother_last_name = models.CharField(max_length=45)
    user_avatar = models.CharField(max_length=45)
    user_delete = models.IntegerField()
    user_token_login = models.CharField(max_length=45, blank=True, null=True)
    user_token_reset = models.CharField(max_length=45, blank=True, null=True)
    user_nationality = models.CharField(max_length=45, blank=True, null=True)
    user_profession_id = models.IntegerField(blank=True, null=True)
    user_birthdate = models.DateTimeField()
    user_insurance = models.IntegerField(blank=True, null=True)
    user_num_sis = models.IntegerField(blank=True, null=True)
    #user_auth_id = models.ForeignKey(User, models.CASCADE)
    ##created_at = models.DateTimeField(auto_now_add=True)
    ##updated_at = models.DateTimeField(auto_now=True)
    #objects = UserManager()


    class Meta:
        managed = False
        db_table = 'users'

class AuthUser(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    phone = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


