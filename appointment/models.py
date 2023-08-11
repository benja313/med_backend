from django.db import models

# Create your models here.
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

    class Meta:
        managed = False
        db_table = 'appointments'