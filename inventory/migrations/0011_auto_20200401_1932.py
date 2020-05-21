# Generated by Django 3.0.2 on 2020-04-01 18:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_auto_20200401_1931'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='category',
            new_name='categorys',
        ),
        migrations.AlterField(
            model_name='vehicleownership',
            name='damage_category',
            field=models.CharField(choices=[('D', 'D: Can be repaired and would cost less than the vehicle’s worth, but other costs such as transporting your vehicle take it over the vehicle’s value.'), ('B', 'B: Can’t be repaired. The body shell has to be crushed, but you can salvage other parts from it.'), ('A', 'A: Can’t be repaired. The entire vehicle has to be crushed.'), ('S', 'S: Can be repaired following structural damage. This replaced category D in October 2017.'), ('C', 'C: Can be repaired, but it would cost more than the vehicle’s worth.'), ('N', 'N: Can be repaired following non-structural damage. This replaced category C in October 2017.')], max_length=1),
        ),
        migrations.AlterField(
            model_name='vehicleownership',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 1, 19, 32, 15, 152189)),
        ),
    ]
