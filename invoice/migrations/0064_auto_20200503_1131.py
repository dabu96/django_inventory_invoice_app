# Generated by Django 3.0.2 on 2020-05-03 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0063_auto_20200503_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 11, 31, 23, 372273)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 11, 31, 23, 372273)),
        ),
    ]
