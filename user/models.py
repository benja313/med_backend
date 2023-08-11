from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_email = models.CharField(max_length=45)
    user_rut = models.IntegerField()
    user_dv = models.CharField(max_length=45)
    user_phone = models.CharField(max_length=45)
    user_password = models.CharField(max_length=45)
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
    ##created_at = models.DateTimeField(auto_now_add=True)
    ##updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        managed = False
        db_table = 'users'
