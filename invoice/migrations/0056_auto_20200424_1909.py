# Generated by Django 3.0.2 on 2020-04-24 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0055_auto_20200424_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydetails',
            name='name',
            field=models.CharField(default='Change company name', max_length=30),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 19, 9, 36, 615176)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 24, 19, 9, 36, 615176)),
        ),
    ]