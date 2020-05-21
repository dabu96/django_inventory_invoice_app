from django.contrib import admin

# Register your models here.

# from .models import VehicleOwnership
# from .forms import VehicleOwnershipForm,


from django.forms import SelectMultiple
from .models import Customer, Invoice, CompanyDetails
from .forms import CustomerForm, InvoiceForm, CompanyDetailsForm





class CustomerAdmin(admin.ModelAdmin):

    form = CustomerForm
    list_display = ['id', 'surname', 'created_by', 'other_names']
    list_filter = ['id', 'surname', 'created_by', 'other_names']
    search_fields = ['id', 'surname', 'created_by', 'other_names']

class InvoiceAdmin(admin.ModelAdmin):

    form = InvoiceForm
    list_display = ['customer', 'reference', 'date_created']
    list_filter = ['customer', 'reference', 'date_created']
    search_fields = ['customer', 'reference', 'date_created']


class CompanyAdmin(admin.ModelAdmin):

    form = CompanyDetailsForm
    list_display = ['__all__']
    list_filter = ['customer', 'date_created']
    search_fields = ['customer', 'date_created']




admin.site.register(Customer, CustomerAdmin)
admin.site.register(Invoice, InvoiceAdmin)

