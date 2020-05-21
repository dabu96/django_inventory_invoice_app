from inventory.resources import PartResource, VehicleResource
from inventory.models import Part
from django.http import HttpResponse


def part_export_to_csv(request):
    part_resource = PartResource()
    data = part_resource.export()
    response = HttpResponse(data.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="parts.csv"'
    return response


def part_export_to_json(request):
    part_resource = PartResource()
    data = part_resource.export()
    response = HttpResponse(data.json, content_type='text/json')
    response['Content-Disposition'] = 'attachment; filename="parts.json"'
    return response


def vehicle_export_to_csv(request):
    vehicle_resource = VehicleResource()
    data = vehicle_resource.export()
    response = HttpResponse(data.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="vehicles.csv"'
    return response

def vehicle_export_to_json(request):
    vehicle_resource = VehicleResource()
    data = vehicle_resource.export()
    response = HttpResponse(data.json, content_type='text/json')
    response['Content-Disposition'] = 'attachment; filename="vehicles.json"'
    return response