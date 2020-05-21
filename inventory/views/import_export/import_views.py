from import_export import resources
from tablib import Dataset
from django.shortcuts import render
from inventory.resources import PartResource, VehicleResource
from django.contrib import messages


def import_part(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        part_resource = PartResource()
        dataset = Dataset()
        new_parts = request.FILES['importData']

        if file_format == 'CSV':
            data_imported = dataset.load(new_parts.read().decode('utf-8'), format='csv')
            result = part_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            data_imported = dataset.load(new_parts.read().decode('utf-8'), format='json')
            result = part_resource.import_data(dataset, dry_run=True)
        if not result.has_errors():
            part_resource.import_data(dataset, dry_run=False)
            messages.success(request, f'Successfully Imported')

    return render(request, 'import.html')


def import_vehicle(request):
    if request.method == 'POST':
        file_format = request.POST['file-format']
        vehicle_resource = VehicleResource()
        dataset = Dataset()
        new_vehicle = request.FILES['importData']

        if file_format == 'CSV':
            data_imported = dataset.load(new_vehicle.read().decode('utf-8'), format='csv')
            result = vehicle_resource.import_data(dataset, dry_run=True)
        elif file_format == 'JSON':
            data_imported = dataset.load(new_vehicle.read().decode('utf-8'), format='json')
            result = vehicle_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            vehicle_resource.import_data(dataset, dry_run=False)
            messages.success(request, f'Successfully Imported')

    return render(request, 'import.html')