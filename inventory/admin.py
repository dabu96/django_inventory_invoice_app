from django.contrib import admin
from .models import VehicleOwnership, Part, VehicleManufacturers, VehicleModel, PartCategory, PartImage
from .forms import VehicleOwnershipForm, PartForm, VehicleModelForm, VehicleManufacturerForm, PartCategoryForm
from django.forms import SelectMultiple
from import_export.admin import ImportExportModelAdmin


class VehicleOwnedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'vehicle_model', 'location']
    form = VehicleOwnershipForm
    list_filter = ['vehicle_model', 'location']
    search_fields = ['vehicle_model', 'location']


class PartAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = PartForm


class PartCategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = PartCategoryForm


class VehicleManufacturerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = VehicleManufacturerForm


class VehicleModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    form = VehicleModelForm


admin.site.register(VehicleOwnership, VehicleOwnedAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(VehicleManufacturers, VehicleManufacturerAdmin)
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(PartCategory, PartCategoryAdmin)

