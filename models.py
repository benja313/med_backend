# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcademicEducation(models.Model):
    academic_education_id = models.IntegerField(primary_key=True)
    academic_education_name = models.CharField(max_length=45)
    academic_education_city = models.CharField(max_length=45, blank=True, null=True)
    academic_education_country = models.CharField(max_length=45, blank=True, null=True)
    academic_education_professional = models.ForeignKey('Users', models.DO_NOTHING)
    trial122 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_education'


class Appointments(models.Model):
    appointment_id = models.IntegerField(primary_key=True)
    appointment_patient = models.ForeignKey('Users', models.DO_NOTHING)
    appointment_date_start = models.DateTimeField()
    appointment_date_end = models.DateTimeField()
    appointment_status = models.IntegerField()
    appointment_day = models.IntegerField()
    appointment_type_pay = models.ForeignKey('TypePayment', models.DO_NOTHING)
    appointment_service = models.ForeignKey('Services', models.DO_NOTHING)
    appointment_first_time = models.IntegerField()
    appointment_checkout = models.ForeignKey('Checkouts', models.DO_NOTHING, blank=True, null=True)
    trial125 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'


class Certifications(models.Model):
    certificaion_id = models.IntegerField(primary_key=True)
    certification_name = models.CharField(max_length=45)
    certification_path = models.CharField(max_length=45, blank=True, null=True)
    certificacion_institution = models.CharField(max_length=45)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certifications'


class Checkouts(models.Model):
    checkout_id = models.IntegerField(primary_key=True)
    checkout_observation = models.CharField(max_length=45)
    checkout_code_transaction = models.CharField(max_length=45)
    checkout_token = models.CharField(max_length=45, blank=True, null=True)
    checkout_authorization_code = models.CharField(max_length=45, blank=True, null=True)
    checkout_payment_type_code = models.CharField(max_length=45, blank=True, null=True)
    checkout_buy_order = models.CharField(max_length=45, blank=True, null=True)
    checkout_vci = models.CharField(max_length=45, blank=True, null=True)
    checkout_card_detail = models.CharField(max_length=45, blank=True, null=True)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkouts'


class Institutions(models.Model):
    institution_id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length=45)
    institution_mail = models.CharField(max_length=45, blank=True, null=True)
    institution_phone = models.CharField(max_length=45, blank=True, null=True)
    institution_state_id = models.IntegerField(blank=True, null=True)
    institution_city_id = models.IntegerField(blank=True, null=True)
    institution_street = models.CharField(max_length=45, blank=True, null=True)
    institution_lat = models.CharField(max_length=45, blank=True, null=True)
    institution_lon = models.CharField(max_length=45, blank=True, null=True)
    institution_user = models.ForeignKey('Users', models.DO_NOTHING)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institutions'


class Insurances(models.Model):
    insurance = models.OneToOneField('TypeInsurances', models.DO_NOTHING, primary_key=True)
    insurance_name = models.CharField(max_length=45)
    insurance_description = models.CharField(max_length=45)
    insurances_type = models.CharField(max_length=45)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurances'


class Locks(models.Model):
    lock_id = models.IntegerField(primary_key=True)
    lock_date_start = models.DateTimeField()
    lock_date_end = models.DateTimeField()
    lock_user = models.ForeignKey('Users', models.DO_NOTHING)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locks'


class Multimedia(models.Model):
    multimedia_id = models.IntegerField(primary_key=True)
    multimedia_path = models.CharField(max_length=45)
    multimedia_type = models.ForeignKey('TypeMultimedia', models.DO_NOTHING)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multimedia'


class Preofessions(models.Model):
    profession_id = models.IntegerField(primary_key=True)
    profesion_name = models.CharField(max_length=45)
    profesion_description = models.CharField(max_length=45)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'preofessions'


class Profesionals(models.Model):
    profesional_id = models.AutoField(primary_key=True)
    profesional_name = models.CharField(max_length=45)
    profesional_description = models.CharField(max_length=45)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesionals'


class RelInstitutionsTypePayment(models.Model):
    institution = models.ForeignKey(Institutions, models.DO_NOTHING)
    type_payment = models.ForeignKey('TypePayment', models.DO_NOTHING)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_institutions_type_payment'


class RelProfessionalInsurance(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    insurance = models.ForeignKey(Insurances, models.DO_NOTHING)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_professional_insurance'


class RelUserCetification(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    certification = models.ForeignKey(Certifications, models.DO_NOTHING, blank=True, null=True)
    trial129 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_user_cetification'


class RelUserMultimedia(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    multimedia = models.ForeignKey(Multimedia, models.DO_NOTHING)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_user_multimedia'


class RelUserRole(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    role = models.ForeignKey('Roles', models.DO_NOTHING)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_user_role'


class RelUserSkill(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    skill = models.ForeignKey('Skills', models.DO_NOTHING)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_user_skill'


class RelUserSpecialty(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    speciality = models.ForeignKey('Specialties', models.DO_NOTHING)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rel_user_specialty'


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    rol_name = models.CharField(max_length=45)
    rol_description = models.CharField(max_length=45)
    rol_delete = models.IntegerField(blank=True, null=True)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class Schedules(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    schedule_start = models.TimeField()
    schedule_end = models.TimeField()
    schedule_day = models.IntegerField()
    schedule_institution = models.ForeignKey(Institutions, models.DO_NOTHING, db_column='schedule_institution')
    schedule_status = models.IntegerField()
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class Services(models.Model):
    service_id = models.IntegerField(primary_key=True)
    servicio_break = models.IntegerField()
    service_weeks_enable = models.IntegerField()
    service_institution = models.ForeignKey(Institutions, models.DO_NOTHING, blank=True, null=True)
    service_price = models.FloatField()
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services'


class Skills(models.Model):
    skill_id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=45)
    skill_description = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skills'


class Specialties(models.Model):
    specialty_id = models.IntegerField(primary_key=True)
    specialty_name = models.CharField(max_length=45)
    specialty_description = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'specialties'


class TypeInsurances(models.Model):
    type_insurance_id = models.IntegerField(primary_key=True)
    type_insurance_name = models.CharField(max_length=45)
    type_insurance_description = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_insurances'


class TypeMultimedia(models.Model):
    type_multi_id = models.IntegerField(primary_key=True)
    type_multi_name = models.CharField(max_length=45)
    type_multi_description = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_multimedia'


class TypePayment(models.Model):
    type_payment_id = models.IntegerField(primary_key=True)
    type_payment_name = models.CharField(max_length=45)
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_payment'


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
    trial132 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
