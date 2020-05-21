from django import forms
from .models import Customer, Invoice, PartBought, CompanyDetails
from inventory.models import Part, VehicleManufacturers, VehicleModel
from django.forms.models import inlineformset_factory, BaseModelFormSet, modelformset_factory


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['title', 'surname', 'other_names', 'address_line', 'address_line2', 'country', 'post_code', 'email',
                  'telephone', 'payment_type', 'card_number']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('customer', 'delivery', 'sale_tax_percent',)


class PartsToRefund(forms.Form):
    parts_select = forms.ModelMultipleChoiceField(queryset=None, label='', widget=forms.CheckboxSelectMultiple, required=True)

    def __init__(self, invoice, *args, **kwargs):
        super(PartsToRefund, self).__init__(*args, **kwargs)
        parts = Part.objects.all().filter(partbought__invoice=invoice)

        self.fields['parts_select'].queryset = parts

    class Meta:
        fields = ('parts_select',)



class PartBoughtForm(forms.ModelForm):

    class Meta:
        model = PartBought
        fields = ('part',)


class CompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = ['logo', 'name', 'address_line1', 'address_line2', 'post_code',
                  'country', 'telephone', 'website', 'vat', 'guarantee_policy',
                  'extra_info']


PartBoughtFormSet = inlineformset_factory(Customer,
                                          PartBought,
                                          form=PartBoughtForm,
                                          extra=1,
                                          can_delete=False,
                                          )

InvoiceFormSet = inlineformset_factory(Customer,
                                       Invoice,
                                       form=InvoiceForm,
                                       extra=1,
                                       can_delete=False
                                       )
