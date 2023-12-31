# Generated by Django 4.2.4 on 2023-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicEducation',
            fields=[
                ('academic_education_id', models.IntegerField(primary_key=True, serialize=False)),
                ('academic_education_name', models.CharField(max_length=45)),
                ('academic_education_city', models.CharField(blank=True, max_length=45, null=True)),
                ('academic_education_country', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'academic_education',
                'managed': False,
            },
        ),
    ]
