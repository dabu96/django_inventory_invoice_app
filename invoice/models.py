from django.db import models
from inventory.models import VehicleOwnership, Part, VehicleManufacturers
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


now = datetime.datetime.now()

from django.utils import timezone


class Customer(models.Model):
    title_choices = (
        ('sir', 'Sir'),
        ('mam', 'Ma\'am'),
        ('mad', 'Madam'),
        ('mr', 'Mr'),
        ('mrs', 'Mrs'),
        ('ms', 'Ms'),
        ('mis', 'Miss'),
        ('dr', 'Dr'),
        ('pro', 'Professor'),
    )


    payment_choices = (
        ('DC', 'Debit Card'),
        ('CC', 'Credit Card'),
        ('CA', 'Cash'),
        ('CH', 'Cheque'),
        ('BA', 'Bank Transfer')
    )

    title = models.CharField(max_length=3, choices=title_choices)
    surname = models.CharField(max_length=20)
    other_names = models.CharField(max_length=40)

    payment_type = models.CharField(max_length=2, choices=payment_choices)
    address_line = models.CharField(max_length=30)
    address_line2 = models.CharField(max_length=30, blank=True, null=True)

    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)  # longest country name is at 48

    email = models.EmailField(null=True, blank=True)
    telephone = models.CharField(max_length=13, null=True, blank=True)  # 11chars for number + country code

    date_created = models.DateTimeField(default=now)
    created_by = models.ForeignKey(User, related_name="customer_created_by",
                                   null=True, blank=True, on_delete=models.SET_NULL)


    card_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)],
                                              blank=True, null=True, help_text='last 4 digits')
        # CharField(max_length=4, null=True, blank=True, help_text='last 4 digits')

    def __str__(self):
        return '%s %s' % (self.other_names, self.surname)




class Invoice(models.Model):
    sale_tax_percent = models.DecimalField(
        max_digits=4, decimal_places=2, default=20,
        validators=[MinValueValidator(0.0)], verbose_name='Tax Percentage'
    )
    reference = models.CharField(max_length=10)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    delivery = models.DecimalField(max_digits=6, decimal_places=2, default='0')  # change to char
    total_cost = models.DecimalField(
        max_digits=7, decimal_places=2, default=0,
        validators=[MinValueValidator(0.0)]
    )

    total_cost_inc_vat = models.DecimalField(max_digits=7, decimal_places=2, default=0,
                                             validators=[MinValueValidator(0.0)])


    slug = models.SlugField(max_length=100)
    date_created = models.DateTimeField(default=now)

    refunded = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        self.reference = str(self.customer_id) + self.customer.other_names[0:1] + self.customer.surname[0:1] \
                         + '_' + str(self.date_created.microsecond)[0:4]

        self.slug = slugify(self.reference)
        super(Invoice, self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % self.reference


class PartBought(models.Model):
    part = models.ForeignKey(Part, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, related_name='parts_bought', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, null=True, blank=True,
                                on_delete=models.SET_NULL)


class CompanyDetails(models.Model):
    logo = models.ImageField(upload_to='images/company/', blank=True, null=True)
    name = models.CharField(max_length=30, default='Change company name')
    address_line1 = models.CharField(max_length=30)
    address_line2 = models.CharField(max_length=30, blank=True, null=True)
    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    guarantee_policy = models.TextField()
    extra_info = models.TextField()
    telephone = models.CharField(max_length=13, null=True, blank=True)  # 11chars for number + country code
    vat = models.IntegerField(validators=[MaxValueValidator(999999999)], blank=True, null=True)
    website = models.CharField(max_length=30, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and CompanyDetails.objects.exists():
            raise ValidationError('There can only be one instance of company')
        return super(CompanyDetails, self).save(*args, **kwargs)