# Generated by Django 3.0.2 on 2020-04-20 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0047_auto_20200420_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='card_number',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 23, 19, 12, 484577)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 23, 19, 12, 484577)),
        ),
    ]
