# Generated by Django 4.2.4 on 2023-08-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMultimedia',
            fields=[
                ('type_multi_id', models.IntegerField(primary_key=True, serialize=False)),
                ('type_multi_name', models.CharField(max_length=45)),
                ('type_multi_description', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'type_multimedia',
                'managed': False,
            },
        ),
    ]
