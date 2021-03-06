# Generated by Django 3.0.2 on 2020-05-01 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0059_auto_20200427_0041'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 4, 45, 0, 792954)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 4, 45, 0, 792954)),
        ),
    ]
