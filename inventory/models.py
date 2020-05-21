from decimal import Decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models import Q
from django.template import defaultfilters
from django.utils.text import slugify

now = datetime.datetime.now()

class VehicleManufacturers(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.name


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.name


class VehicleModel(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(VehicleManufacturers, on_delete=models.PROTECT)
    year = models.PositiveIntegerField(default=2010, validators=[MaxValueValidator(now.year), MinValueValidator(1970)])
    litre = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(Decimal('0.01'))])

    vehicle_type_choices = (
        ('HA', 'Hatchback'),
        ('SA', 'Saloon'),
        ('ES', 'Estate'),
        ('MP', 'MPV'),
        ('SU', 'SUV'),
        ('CO', 'Coupe'),
        ('SP', 'Sports Car'),
        ('CN', 'Convertible'),
        ('VA', 'Van')
    )

    vehicle_type = models.CharField(max_length=2, choices=vehicle_type_choices)
    transmission_choices = (
        ('A', 'Automatic'),
        ('M', 'Manual'),
        ('S', 'Semi-automatic')
    )
    transmission = models.CharField(max_length=1, choices=transmission_choices)

    fuel_choices = (
        ('P', 'Petrol'),
        ('D', 'Diesel'),
        ('H', 'Hybrid'),
        ('E', 'Electric'),
        ('B', 'Bio-diesel'),

    )

    fuel = models.CharField(max_length=1, choices=fuel_choices, default='P')
    slug = models.SlugField(max_length=100, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.year) + self.name + str(self.litre))
        super(VehicleModel, self).save(*args, **kwargs)

    def __str__(self):
        return '%s %sL %s %s' % (self.name, self.litre, self.year,
                                 self.get_transmission_display())


class VehicleOwnership(models.Model):
    sku = models.CharField(max_length=40)

    manufacturer = models.ForeignKey(VehicleManufacturers, on_delete=models.PROTECT)
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT)
    vin = models.CharField(max_length=17)
    colour = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.PROTECT)  # change this to foreign relationship to add more
    damage_cat_choices = {
        ('A', 'A: Can’t be repaired. The entire vehicle has to be crushed.'),
        ('B', 'B: Can’t be repaired. The body shell has to be crushed, but you can salvage other parts from it.'),
        ('C', 'C: Can be repaired, but it would cost more than the vehicle’s worth.'),
        ('D', 'D: Can be repaired and would cost less than the vehicle’s worth, but other costs such as transporting '
              'your vehicle take it over the vehicle’s value.'),
        ('N', 'N: Can be repaired following non-structural damage. This replaced category C in October 2017.'),
        ('S', 'S: Can be repaired following structural damage. This replaced category D in October 2017.')
    }

    damage_category = models.CharField(max_length=1, choices=damage_cat_choices)
    damage_primary = models.CharField(max_length=50, default='None')
    damage_secondary = models.CharField(max_length=50, default='None')

    date_created = models.DateTimeField(default=now)

    cost_price = models.PositiveIntegerField()
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        name = self.vehicle_model.name
        whitespaces = name.count(' ')
        if whitespaces > 1:
            split_name = name.split(' ', whitespaces)
            tmp_name = ''
            for name in split_name:
                tmp_name += name[0:3] + '_'
            name = tmp_name
        else:
            name = name[0:5] + '_'

        litre = str(self.vehicle_model.litre).replace('.', 'L')
        manufacturer = str(self.vehicle_model.manufacturer)[0:3]
        year = str(self.vehicle_model.year)[0:-2]
        fuel = str(self.vehicle_model.fuel)
        transmission = str(self.vehicle_model.transmission)
        colour = str(self.colour)[0:3]

        sku = str(manufacturer +
                  '_' + name +
                  year +
                  '_' + litre +
                  '_' + fuel +
                  '_' + transmission +
                  '_' + colour).upper()

        counter = 0
        temp_sku = sku
        while True:
            counter += 1
            get_sku = VehicleOwnership.objects.filter(sku=temp_sku).exists()
            if not get_sku:
                self.sku = temp_sku
                break
            else:
                temp_sku = sku + '_' + str(counter)

        self.slug = slugify(self.vehicle_model)
        super(VehicleOwnership, self).save(*args, **kwargs)
    def get_slug(self):
        return slugify(self.vehicle_model)

    def get_absolute_url(self):
        return reverse("vehicle-detail", kwargs={
            'pk': self.pk,
            'slug': self.slug
        })

    def __str__(self):
        return '%s %s' % (self.vehicle_model, self.colour)


class VehicleImage(models.Model):
    vehicle = models.ForeignKey(VehicleOwnership, related_name="vehicle_image", on_delete=models.CASCADE)
    img = models.FileField(upload_to='images/vehicles/', blank=True, null=True)


class PartCategory(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return '%s' % self.name


class Part(models.Model):
    sku = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    side = models.CharField(max_length=15, null=True, blank=True)
    available = models.BooleanField(default=True)
    vehicle = models.ForeignKey(VehicleOwnership, on_delete=models.PROTECT)
    category = models.ForeignKey(PartCategory, on_delete=models.PROTECT)
    selling_price = models.DecimalField(decimal_places=2, max_digits=7)
    slug = models.SlugField(max_length=100)
    part_number = models.CharField(max_length=15, default='unknown')
    extra_info = models.CharField(max_length=200, null=True, blank=True)
    condition_choices = (
        ('U', 'Used'),
        ('R', 'Re-Manufactured'),
        ('O', 'Other'),
    )
    condition = models.CharField(max_length=1, choices=condition_choices, default='U')

    def save(self, *args, **kwargs):
        name_array = [self.name, self.vehicle.vehicle_model.name]

        for index, name in enumerate(name_array):
            whitespaces = name.count(' ')
            if whitespaces > 1:
                split_name = name.split(' ', whitespaces)
                tmp_name = ''
                for name in split_name:
                    tmp_name += name[0:3] + '_'
                name_array[index] = tmp_name
            else:
                name_array[index] = name[0:5] + '_'

        part_name = name_array[0]
        model_name = name_array[1]

        litre = str(self.vehicle.vehicle_model.litre).replace('.', 'L')
        colour = self.vehicle.colour[0:3]
        year = str(self.vehicle.vehicle_model.year)[0:-2]
        side = self.side
        if side is None:
            sku = str(part_name +
                      model_name +
                      litre +
                      '_' + year +
                      '_' + colour).upper()

        else:
            side = side[0:3]
            sku = str(part_name +
                      side +
                      '_' + model_name +
                      litre +
                      '_' + year +
                      '_' + colour).upper()
        counter = 0
        temp_sku = sku
        while True:
            counter += 1
            get_sku = Part.objects.filter(sku=temp_sku).exists()
            if not get_sku:
                self.sku = temp_sku
                break
            else:
                temp_sku = sku + '_' + str(counter)
        self.slug = slugify(self.name, self.vehicle)
        super(Part, self).save(*args, **kwargs)

    def get_slug(self):
        return slugify(self.name, self.vehicle)

    def get_id(self):
        return self.id

    def get_absolute_url(self):
        return reverse("part-detail", kwargs={
            'id': self.id,
            'slug': self.slug
        })

    def __str__(self):
        return '%s %s' % (self.name, self.vehicle)


class PartImage(models.Model):
    img = models.ImageField(upload_to='images/parts/', blank=True, null=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
