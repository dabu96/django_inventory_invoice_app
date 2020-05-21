# Generated by Django 3.0.2 on 2020-05-03 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0072_auto_20200503_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleownership',
            name='damage_category',
            field=models.CharField(choices=[('S', 'S: Can be repaired following structural damage. This replaced category D in October 2017.'), ('B', 'B: Can’t be repaired. The body shell has to be crushed, but you can salvage other parts from it.'), ('C', 'C: Can be repaired, but it would cost more than the vehicle’s worth.'), ('D', 'D: Can be repaired and would cost less than the vehicle’s worth, but other costs such as transporting your vehicle take it over the vehicle’s value.'), ('A', 'A: Can’t be repaired. The entire vehicle has to be crushed.'), ('N', 'N: Can be repaired following non-structural damage. This replaced category C in October 2017.')], max_length=1),
        ),
        migrations.AlterField(
            model_name='vehicleownership',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 3, 11, 52, 7, 909297)),
        ),
    ]
