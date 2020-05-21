# Generated by Django 3.0.2 on 2020-04-19 02:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0037_auto_20200419_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='partbought',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.Invoice'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 3, 42, 46, 558396)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 3, 42, 46, 558396)),
        ),
    ]
