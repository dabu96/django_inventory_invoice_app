# Generated by Django 3.0.2 on 2020-04-19 03:36

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0038_auto_20200419_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetails',
            name='telephone',
            field=models.CharField(default='undefined', max_length=13),
        ),
        migrations.AddField(
            model_name='companydetails',
            name='vat',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999999)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 4, 36, 37, 110937)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 4, 36, 37, 110937)),
        ),
    ]
