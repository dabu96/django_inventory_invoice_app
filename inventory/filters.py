from .models import *
import django_filters as filters


# class ManufacturerFilter(django_filters.FilterSet):
#     class Meta:
#         model = VehicleManufacturer
#         fields = ['name']

class VehicleFilter(filters.FilterSet):
    # model = django_filters.ModelChoiceFilter(
    #     queryset=VehicleModel.objects.order_by('')
    # )

    manufacturer = filters.ModelMultipleChoiceFilter(
        field_name='vehicle_model_id__manufacturer_id__name',
        # to_field_name='name',
        label="Manufacturers",
        queryset=VehicleManufacturers.objects.all()
    )

    model = filters.CharFilter(field_name='vehicle_model_id__name', lookup_expr='icontains', label="Model Name")

    year = filters.CharFilter(field_name='vehicle_model_id__year', lookup_expr='icontains', label="Year")

    class Meta:
        model = VehicleOwnership
        fields = ['sku', 'manufacturer', 'model']


class VehicleModelFilter(filters.FilterSet):
    manufacturer = filters.ModelMultipleChoiceFilter(
        field_name='manufacturer_id__name',
        label="Manufacturers",
        queryset=VehicleManufacturers.objects.all()
    )

    model = filters.CharFilter(field_name='name', lookup_expr='icontains', label="Model Name")
    year = filters.CharFilter(field_name='year', lookup_expr='icontains', label="Year")

    class Meta:
        model = VehicleModel
        fields = ['manufacturer', 'model', 'year']


class PartFilter(filters.FilterSet):

    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        if len(data) == 0:
            data['available'] = 'True'
        super().__init__(data, *args, **kwargs)

    manufacturer = filters.ModelMultipleChoiceFilter(
        field_name='vehicle_id__vehicle_model_id__manufacturer_id__name',
        # to_field_name='name',
        label="Manufacturers",
        queryset=VehicleManufacturers.objects.all()
    )

    model = filters.CharFilter(field_name='vehicle_id__vehicle_model_id__name', lookup_expr='icontains', label="Model")

    year = filters.CharFilter(field_name='vehicle_id__vehicle_model_id__year', lookup_expr='icontains', label="Year")

    category = filters.ModelChoiceFilter(
        field_name='category_id__name',
        label='Categories',
        queryset=PartCategory.objects.all()
    )

    AVAILABLE_CHOICES = {
        ('', 'All'),
        ('True', 'Available'),
        ('False', 'Unavailable')
    }
    available = filters.ChoiceFilter(
        field_name='available',
        lookup_expr='exact',
        choices=AVAILABLE_CHOICES,
        empty_label=None
    )

    class Meta:
        model = Part
        fields = ('manufacturer', 'model', 'category',)
