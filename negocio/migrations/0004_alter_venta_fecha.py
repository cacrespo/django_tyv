# Generated by Django 3.2.6 on 2021-10-17 21:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('negocio', '0003_auto_20211017_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.TimeField(blank=True, null=True, verbose_name=datetime.datetime.now),
        ),
    ]
