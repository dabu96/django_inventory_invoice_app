# Generated by Django 3.0.2 on 2020-04-23 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0051_auto_20200423_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 17, 55, 3, 244884)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 17, 55, 3, 244884)),
        ),
    ]