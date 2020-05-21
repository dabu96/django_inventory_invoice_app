from django.http import JsonResponse
from django.template.loader import render_to_string
from inventory.models import Location
from inventory.forms import LocationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required()
def save_location_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['location_list'] = render_to_string('settings/location/list.html', {
                'locations': Location.objects.all()
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
def location_create(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
    else:
        form = LocationForm()
    return save_location_form(request, form, 'settings/location/create.html')


@login_required()
def location_update(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
    else:
        form = LocationForm(instance=location)
    return save_location_form(request,
                              form,
                              'settings/location/update.html')

@login_required()
def location_delete(request, pk):
    location = get_object_or_404(Location, pk=pk)

    data = dict()
    # try:
    if request.method == 'POST':
        location.delete()
        data['form_is_valid'] = True
        locations = Location.objects.all()
        data['location_list'] = render_to_string('settings/location/list.html', {
            'locations': locations
        })
    else:
        context = {'location': location}
        data['html_form'] = render_to_string('settings/location/delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
