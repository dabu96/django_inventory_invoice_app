# Generated by Django 3.0.2 on 2020-04-19 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0039_auto_20200419_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='website',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 5, 1, 58, 942656)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 5, 1, 58, 942656)),
        ),
    ]
