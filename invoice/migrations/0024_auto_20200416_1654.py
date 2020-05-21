# Generated by Django 3.0.2 on 2020-04-16 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0023_auto_20200416_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='payment_type',
            field=models.CharField(default='unspecified', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 54, 22, 20297)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 54, 22, 20297)),
        ),
    ]
