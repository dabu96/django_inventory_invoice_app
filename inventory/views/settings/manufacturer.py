from django.http import JsonResponse
from django.template.loader import render_to_string
from inventory.models import VehicleManufacturers
from inventory.forms import VehicleManufacturerForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required()
def save_manufacturer_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['manufacturer_list'] = render_to_string('settings/manufacturer/list.html', {
                'manufacturers': VehicleManufacturers.objects.all()
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


@login_required()
def manufacturer_create(request):
    if request.method == 'POST':
        form = VehicleManufacturerForm(request.POST)
    else:
        form = VehicleManufacturerForm()
    return save_manufacturer_form(request, form, 'settings/manufacturer/create.html')


@login_required()
def manufacturer_update(request, pk):
    manufacturer = get_object_or_404(VehicleManufacturers, pk=pk)
    if request.method == 'POST':
        form = VehicleManufacturerForm(request.POST, instance=manufacturer)
    else:
        form = VehicleManufacturerForm(instance=manufacturer)
    return save_manufacturer_form(request,
                                  form,
                                  'settings/manufacturer/update.html')

@login_required()
def manufacturer_delete(request, pk):
    model = VehicleManufacturers
    manufacturer = get_object_or_404(model, pk=pk)
    data = dict()
    if request.method == 'POST':
        manufacturer.delete()
        data['form_is_valid'] = True
        manufacturers = VehicleManufacturers.objects.all()
        data['manufacturer_list'] = render_to_string('settings/manufacturer/list.html', {
            'manufacturers': manufacturers
        })
    else:
        context = {'manufacturer': manufacturer}
        data['html_form'] = render_to_string('settings/manufacturer/delete.html',
                                                     context,
                                                     request=request,
                                                     )
    return JsonResponse(data)