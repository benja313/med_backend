# Generated by Django 4.2.4 on 2023-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('appointment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('appointment_date_start', models.DateTimeField()),
                ('appointment_date_end', models.DateTimeField()),
                ('appointment_status', models.IntegerField()),
                ('appointment_day', models.IntegerField()),
                ('appointment_first_time', models.IntegerField()),
            ],
            options={
                'db_table': 'appointments',
                'managed': False,
            },
        ),
    ]