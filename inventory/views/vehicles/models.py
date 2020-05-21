from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
# from ..forms import VehicleForm, VehicleMakeForm, PartFormSet, VehicleNameFormSet #, VehicleNameForm #, VehicleFormSet
# from ..models import Vehicle, VehicleMake, VehicleName

from inventory.forms import VehicleOwnershipForm, VehicleModelForm, VehicleManufacturerForm, \
    PartFormSet, VehicleModelFormSet, VehicleImageFormSet

from inventory.filters import *

from django.urls import reverse
from django.views.generic import (
    UpdateView,
    CreateView,
    DeleteView
)
from django.http import JsonResponse
from django.template.loader import render_to_string
from inventory.filters import VehicleModelFilter

from django_filters.views import FilterView
from django_tables2 import SingleTableView
from inventory.tables import VehicleTable, PartTable, VehicleModelTable
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ModelListView(LoginRequiredMixin, SingleTableView):
    table_class = VehicleModelTable
    context_object_name = 'table'
    template_name = 'vehicle/model/list.html'
    queryset = VehicleModel.objects.all()

    def get_filter(self):
        model_filter = VehicleModelFilter(self.request.GET, queryset=self.queryset)
        return model_filter

    def get_queryset(self):
        return self.get_filter().qs

    def get(self, request, *args, **kwargs):
        table = VehicleModelTable(self.get_queryset())
        context = {'object_list': self.get_queryset(),
                   'model_filter': self.get_filter(),
                   'table': table
                   }
        return render(request, self.template_name, context)


class ModelObjectMixin(LoginRequiredMixin, object):
    def get_object(self):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        obj = None
        if id is not None:
            obj = get_object_or_404(VehicleModel, id=pk, slug=slug)
        else:
            print('doesnt exist')
        return obj


@login_required()
def model_delete(request, pk, slug):
    vehicle_model = get_object_or_404(VehicleModel, id=pk)
    context = {}
    data = dict()
    if request.method == 'POST':
        vehicle_model.delete()
        data['form_is_valid'] = True
        vehicle_models = VehicleModel.objects.all()

        table = VehicleModelTable(vehicle_models)
        model_filter = VehicleModelFilter(request.GET, queryset=vehicle_models)
        context['table'] = table
        context['model_filter'] = model_filter

        data['models_list'] = render_to_string('vehicle/model/list.html',
                                               context,
                                               request=request
                                               )


    else:
        context = {'vehicle_model': vehicle_model}
        data['html_form'] = render_to_string('vehicle/model/delete.html',
                                                     context,
                                                     request=request,
                                                     )
    return JsonResponse(data)


@login_required()
def save_model_form(request, form, template_name):
    data = dict()
    context = {}
    if request.method == 'POST':
        data['form_is_valid'] = True
        table = VehicleModelTable(VehicleModel.objects.all())
        model_filter = VehicleModelFilter(request.GET, queryset=VehicleModel.objects.all())
        context['table'] = table
        context['model_filter'] = model_filter
        context['form'] = form
        data['models_list'] = render_to_string('vehicle/model/list.html',
                                               context,
                                               request=request
                                               )
    else:
        context['form'] = form
        data['html_form'] = render_to_string(template_name,
                                             context,
                                             request=request
                                             )
    return JsonResponse(data)


class ModelCreateView(LoginRequiredMixin, CreateView):
    template_name = 'vehicle/model/create.html'
    form_class = VehicleModelForm
    queryset = VehicleModel.objects.all()

    def post(self, request, *args, **kwargs):
        print('post')
        model_form = VehicleModelForm(self.request.POST)

        if model_form.is_valid():
            return self.form_valid(model_form)

    def get(self, request, *args, **kwargs):
        model_form = VehicleModelForm()
        return save_model_form(self.request, form=model_form,
                               template_name=self.template_name)

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return save_model_form(self.request, form=form, template_name=self.template_name)


class ModelUpdateView(ModelObjectMixin, UpdateView):
    template_name = 'vehicle/model/update.html'
    form_class = VehicleModelForm
    model = VehicleModel
    queryset = VehicleModel.objects.all()

    def post(self, request, *args, **kwargs):
        print('post')
        model_form = VehicleModelForm(self.request.POST, instance=self.get_object())

        if model_form.is_valid():
            return self.form_valid(model_form)

    def get(self, request, *args, **kwargs):
        model_form = VehicleModelForm(instance=self.get_object())
        return save_model_form(self.request, form=model_form,
                               template_name=self.template_name)

    def form_valid(self, form):
        print(form.cleaned_data)
        form.save()
        return save_model_form(self.request, form=form, template_name=self.template_name)
