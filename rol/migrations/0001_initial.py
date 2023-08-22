# Generated by Django 4.2.4 on 2023-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('rol_name', models.CharField(max_length=45)),
                ('rol_description', models.CharField(max_length=45)),
                ('rol_delete', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'roles',
                'managed': False,
            },
        ),
    ]