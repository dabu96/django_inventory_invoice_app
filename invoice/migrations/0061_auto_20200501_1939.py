# Generated by Django 3.0.2 on 2020-05-01 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0060_auto_20200501_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 19, 38, 31, 106749)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.OneToOneField(on_delete=models.SET('None'), to='invoice.Customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 19, 38, 31, 106749)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='delivery',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=6),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='reference',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
