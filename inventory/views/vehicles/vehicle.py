from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import json
from django.contrib import messages
from django.core import serializers

from inventory.forms import VehicleOwnershipForm, VehicleModelForm, VehicleManufacturerForm, VehicleImageFormSet, \
    VehicleImageForm
from django.views.generic.edit import FormMixin
from django.core.files.storage import FileSystemStorage
from inventory.filters import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    DetailView,
    ListView,
    DeleteView,
    UpdateView,
    CreateView
)
from django.http import JsonResponse
from django.template.loader import render_to_string
from inventory.filters import VehicleFilter
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from inventory.tables import VehicleTable, PartTable
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def load_vehicle_model(request):
    manufacturer_id = request.GET.get('manufacturer')
    models = VehicleModel.objects.filter(manufacturer_id=manufacturer_id)
    print(request.path)
    print(request)
    return render(request, 'vehicle/model_dropdown_options.html', {'models': models})


class VehicleListView(LoginRequiredMixin, SingleTableView):
    # model = VehicleOwnership
    table_class = VehicleTable
    context_object_name = 'table'

    template_name = 'vehicle/list.html'
    queryset = VehicleOwnership.objects.all()
    images = VehicleImage.objects.all()

    def get_filter(self):
        vehicle_filter = VehicleFilter(self.request.GET, queryset=self.queryset)
        return vehicle_filter

    def get_queryset(self):
        return self.get_filter().qs

    def get(self, request, *args, **kwargs):
        table = VehicleTable(self.get_queryset())
        context = {'object_list': self.get_queryset(),
                   'image_list': self.images,
                   'vehicle_filter': self.get_filter(),
                   'table': table
                   }
        return render(request, self.template_name, context)


class VehicleObjectMixin(LoginRequiredMixin, object):
    def get_object(self):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        obj = None
        if pk is not None:
            obj = get_object_or_404(VehicleOwnership, pk=pk, slug=slug)
        else:
            print('doesnt exist')
        return obj


class VehicleDetailView(VehicleObjectMixin, DetailView):
    template_name = 'vehicle/detail.html'
    query_pk_and_slug = True

    def get_parts(self):
        pk = self.kwargs.get('pk')
        if id is not None:
            parts = Part.objects.filter(vehicle_id=pk)
            return parts
        else:
            print('doesnt exist')

    def get(self, request, *args, **kwargs):
        table = PartTable(self.get_parts())
        table.exclude = ('select',)

        images = VehicleImage.objects.filter(vehicle=self.get_object())
        context = {'vehicle': self.get_object(),
                   'table': table,
                   'images': images
                   }
        return render(request, self.template_name, context)


@login_required()
def vehicle_delete(request, pk):
    model = VehicleOwnership
    vehicle = get_object_or_404(model, pk=pk)

    data = dict()
    try:
        if request.method == 'POST':
            vehicle.delete()
            data['form_is_valid'] = True
        else:
            context = {'vehicle': vehicle}
            data['html_form'] = render_to_string('vehicle/delete.html',
                                                 context,
                                                 request=request,
                                                 )
    except Exception as e:

        data = messages.error(request, "Unable to process delete request. Try deleting all parts associated "
                                       "with the vehicle: ")
    return JsonResponse(data=data, safe=False)


@login_required()
def save_vehicle_form(request, form, template_name):
    data = dict()
    context = {}
    if request.method == 'POST':
        data['form_is_valid'] = True
        vehicle = VehicleOwnership.objects.all()

        table = VehicleTable(vehicle)
        context['table'] = table
        vehicle_filter = VehicleFilter(request.GET, queryset=vehicle)
        context['vehicle_filter'] = vehicle_filter

    context['vehicle_form'] = form
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )

    return JsonResponse(data)


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = VehicleOwnership
    template_name = 'vehicle/create_ajax.html'
    fields = ('manufacturer', 'vehicle_model', 'vin', 'cost_price', 'colour', 'mileage', 'location',
              'damage_category', 'damage_primary', 'damage_secondary',)
    form_class = VehicleOwnershipForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(VehicleCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['vehicle_form'] = VehicleOwnershipForm(self.request.POST, self.request.FILES)
        else:
            context['vehicle_form'] = VehicleOwnershipForm()
        return context

    def post(self, request, *args, **kwargs):
        print('post')
        vehicle_form = VehicleOwnershipForm(self.request.POST, self.request.FILES)

        if vehicle_form.is_valid():
            return self.form_valid(vehicle_form)

    def get(self, request, *args, **kwargs):
        vehicle_form = VehicleOwnershipForm()
        return save_vehicle_form(self.request, form=vehicle_form,
                                 template_name=self.template_name)

    def form_valid(self, form):
        forms = form.save()
        return save_vehicle_form(self.request, form=VehicleOwnershipForm(),
                                 template_name=self.template_name)


def vehicle_image_upload(request, pk, slug):
    vehicle = get_object_or_404(VehicleOwnership, pk=pk)
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES
        for file in uploaded_file:
            print(file)
            print(request.FILES[file])
            new_image = request.FILES[file]
            VehicleImage(vehicle=vehicle, img=new_image).save()
        return redirect('vehicle-detail', pk=pk, slug=slug)
    return render(request, 'vehicle/upload-image.html')


def vehicle_image_delete(request, pk, image_id, slug):
    if request.method == 'POST':
        image = get_object_or_404(VehicleImage, pk=image_id, vehicle=pk)
        image.img.delete()
        image.delete()
    return redirect('vehicle-detail', pk=pk, slug=slug)


class VehicleUpdateView(VehicleObjectMixin, UpdateView):
    model = VehicleOwnership
    template_name = 'vehicle/update.html'
    fields = ('manufacturer', 'vehicle_model', 'vin', 'cost_price', 'colour', 'mileage', 'location',
              'damage_category', 'damage_primary', 'damage_secondary',)
    form_class = VehicleOwnershipForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(VehicleCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            print('get context post')
            context['vehicle_form'] = VehicleOwnershipForm(self.request.POST, self.request.FILES,
                                                           instance=self.get_object)
        else:
            print('get context')

            context['vehicle_form'] = VehicleOwnershipForm(instance=self.get_object())

        return context

    def post(self, request, *args, **kwargs):
        print('post')

        vehicle_form = VehicleOwnershipForm(self.request.POST, self.request.FILES, instance=self.get_object())

        if vehicle_form.is_valid():
            return self.form_valid(vehicle_form)

    def get(self, request, *args, **kwargs):
        print(self.get_object().pk)
        vehicle_form = VehicleOwnershipForm(instance=self.get_object())
        print(vehicle_form.instance)
        return save_vehicle_form(self.request, form=vehicle_form,
                                 template_name=self.template_name)

    def form_valid(self, form):
        forms = form.save()

        return save_vehicle_form(self.request, form=VehicleOwnershipForm(instance=self.get_object()),
                                 template_name=self.template_name)

