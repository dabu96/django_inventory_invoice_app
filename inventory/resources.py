from import_export import resources
from .models import Part, VehicleOwnership
from django.db import models

class PartResource(resources.ModelResource):
    class Meta:
        model = Part
        exclude = ("slug",)

class VehicleResource(resources.ModelResource):
    class Meta:
        model = VehicleOwnership
        exclude = ("slug",)
