# Generated by Django 3.0.2 on 2020-04-16 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0020_auto_20200416_1650'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyDetails',
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 51, 13, 409769)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 51, 13, 409769)),
        ),
    ]
