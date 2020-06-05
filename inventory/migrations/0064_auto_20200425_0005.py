# Generated by Django 3.0.2 on 2020-04-24 23:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0063_auto_20200424_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleownership',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/vehicles/'),
        ),
        migrations.AlterField(
            model_name='vehicleimage',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_images', to='inventory.VehicleOwnership'),
        ),
        migrations.AlterField(
            model_name='vehicleownership',
            name='damage_category',
            field=models.CharField(choices=[('A', 'A: Can’t be repaired. The entire vehicle has to be crushed.'), ('S', 'S: Can be repaired following structural damage. This replaced category D in October 2017.'), ('B', 'B: Can’t be repaired. The body shell has to be crushed, but you can salvage other parts from it.'), ('C', 'C: Can be repaired, but it would cost more than the vehicle’s worth.'), ('N', 'N: Can be repaired following non-structural damage. This replaced category C in October 2017.'), ('D', 'D: Can be repaired and would cost less than the vehicle’s worth, but other costs such as transporting your vehicle take it over the vehicle’s value.')], max_length=1),
        ),
        migrations.AlterField(
            model_name='vehicleownership',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 25, 0, 5, 10, 211363)),
        ),
    ]