# from django.forms import ModelForm, ModelChoiceField, HiddenInput, ImageField
from django import forms
from .models import VehicleOwnership, Part, VehicleManufacturers, VehicleModel, VehicleImage, Location, PartCategory, \
    PartImage
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.forms.models import modelformset_factory
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings
from django.urls import reverse
from django.forms import formset_factory

class VehicleOwnershipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['vehicle_model'].queryset = VehicleModel.objects.none()

        if 'manufacturer' in self.data:
            try:
                manufacturer_id = int(self.data.get('manufacturer'))
                self.fields['vehicle_model'].queryset = VehicleModel.objects.filter(
                    manufacturer_id=manufacturer_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['vehicle_model'].queryset = VehicleModel.objects.filter(manufacturer__vehiclemodel__exact=
                                                                                self.instance.vehicle_model)
        else:
            self.fields['vehicle_model'].queryset = VehicleModel.objects.all()

    manufacturer = forms.ModelChoiceField(
        required=False,
        queryset=VehicleManufacturers.objects.all(),
        widget=forms.Select(choices=VehicleManufacturers.objects.all())
    )

    vehicle_model = forms.ModelChoiceField(
        required=True,
        queryset=VehicleModel.objects.all(),
        label=mark_safe('Models (<a href="/inventory/vehicles/model/" target="_blank">View Model</a>)')

    )

    class Meta:
        model = VehicleOwnership
        fields = ('manufacturer', 'vehicle_model', 'vin', 'cost_price', 'colour', 'mileage', 'location',
                  'damage_category', 'damage_primary', 'damage_secondary',)


class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ('name', 'side', 'vehicle', 'part_number', 'condition', 'category', 'selling_price', 'extra_info',)


class PartImageForm(forms.ModelForm):
    class Meta:
        model = PartImage
        fields = ('img',)


class PartCategoryForm(forms.ModelForm):
    class Meta:
        model = PartCategory
        fields = ('name',)


class VehicleImageForm(forms.ModelForm):
    class Meta:
        model = VehicleImage
        fields = ('img',)



class VehicleManufacturerForm(forms.ModelForm):
    class Meta:
        model = VehicleManufacturers
        fields = ['name']


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name',)


class VehicleModelForm(forms.ModelForm):
    manufacturer = forms.ModelChoiceField(
        required=False,
        queryset=VehicleManufacturers.objects.all()
    )

    class Meta:
        model = VehicleModel
        fields = ('manufacturer', 'name', 'litre', 'year', 'fuel', 'transmission', 'vehicle_type',)



VehicleModelFormSet = inlineformset_factory(VehicleManufacturers,
                                            VehicleModel,
                                            form=VehicleModelForm,
                                            extra=1,
                                            can_delete=True)




PartFormSet = inlineformset_factory(VehicleOwnership,
                                    Part,
                                    form=PartForm,
                                    extra=2,
                                    can_delete=True)

# VehicleImageFormSet = inlineformset_factory(VehicleOwnership,
#                                             VehicleImage,
#                                             form=VehicleImageForm,
#                                             extra=1,
#                                             can_delete=True)

VehicleImageFormSet = modelformset_factory(
    VehicleImage,
    fields=('img', ),
    extra=1,
)


# VehicleImageFormSet = formset_factory(VehicleImageForm, extra=1)

PartImageFormSet = modelformset_factory(PartImage, form=PartImageForm)

