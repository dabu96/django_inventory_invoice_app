from .models import *
from django import forms
import django_filters as filters
from .forms import InvoiceForm

# class ManufacturerFilter(django_filters.FilterSet):
#     class Meta:
#         model = VehicleManufacturer
#         fields = ['name']

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceFilter(filters.FilterSet):

    def __init__(self, data, *args, **kwargs):
        data = data.copy()

        print(data)
        if len(data) == 0:
            data['refunded'] = 'False'

        super().__init__(data, *args, **kwargs)

    customer_surname = filters.CharFilter(field_name='customer_id__surname', lookup_expr='icontains',
                                          label="Customer Surname")
    customer_other_names = filters.CharFilter(field_name='customer_id__other_names', lookup_expr='icontains',
                                              label="Other Names")

    reference = filters.CharFilter(lookup_expr='icontains', field_name='reference', label="Invoice Reference")

    REFUNDED_CHOICES = {
        ('False', 'Invoiced'),
        ('True', 'Refunded')
    }
    refunded = filters.ChoiceFilter(
        field_name='refunded',
        lookup_expr='exact',
        choices=REFUNDED_CHOICES,
        empty_label=None,
        label='Status'

    )

    date_created = filters.DateFilter(lookup_expr='icontains', label='Date created', widget=DateInput(
            attrs={
                'class': 'datepicker'
            }
        )
    )


    class Meta:
        model = Invoice
        fields = ['customer_surname', 'customer_other_names', 'date_created', 'reference', 'refunded']

