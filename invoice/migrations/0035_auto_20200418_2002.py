# Generated by Django 3.0.2 on 2020-04-18 19:02

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0034_auto_20200416_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 20, 2, 12, 88417)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 20, 2, 12, 88417)),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sale_tax_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Tax Percentage'),
        ),
        migrations.AlterField(
            model_name='partbought',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parts_bought', to='invoice.Customer'),
        ),
    ]
