# Generated by Django 3.0.2 on 2020-04-05 23:51

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 0, 51, 36, 378052)),
        ),
        migrations.AddField(
            model_name='customer',
            name='payment_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='post_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoice.Customer'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 6, 0, 51, 36, 378052)),
        ),
        migrations.AddField(
            model_name='invoice',
            name='delivery',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=6),
        ),
        migrations.AddField(
            model_name='invoice',
            name='sale_tax_percent',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address_line',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
