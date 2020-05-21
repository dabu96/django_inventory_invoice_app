from django.shortcuts import render, get_object_or_404, redirect
from inventory.forms import PartForm, PartImageFormSet
from inventory.models import Part, PartImage
from django.urls import resolve, reverse
from django.views.generic import (
    DetailView,
    ListView,
    DeleteView,
    UpdateView,
    CreateView
)
from django.template.loader import render_to_string
from django.http import JsonResponse

from django_tables2 import SingleTableView, RequestConfig
from inventory.tables import PartTable
from inventory.filters import PartFilter
from inventory.resources import PartResource
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required()
def export_to_csv(self):
    dataset = PartResource().export()


class PartObjectMixin(LoginRequiredMixin, object):
    def get_object(self):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        obj = None
        if id is not None:
            obj = get_object_or_404(Part, id=pk, slug=slug)
        return obj


class PartListView(LoginRequiredMixin, SingleTableView):
    template_name = 'part/list.html'
    form_class = PartForm
    queryset = Part.objects.all()
    table_class = PartTable

    def get_filter(self):
        myFilter = PartFilter(self.request.GET, queryset=self.queryset)
        return myFilter

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = PartTable(self.get_queryset())
        myFilter = self.get_filter()
        object_list = self.get_queryset()
        RequestConfig(self.request).configure(table)
        context.update(locals())
        return context


class PartDetailView(PartObjectMixin, DetailView):
    template_name = 'part/detail.html'

    def get(self, request, id=None, *args, **kwargs):
        images = PartImage.objects.filter(part=self.get_object())

        context = {'part': self.get_object(),
                   'images': images
                   }
        return render(request, self.template_name, context)


@login_required()
def save_part_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


@login_required()
def part_create(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
    else:
        form = PartForm()
    return save_part_form(request, form, 'part/create.html')


@login_required()
def part_update(request, pk, slug):
    part = get_object_or_404(Part, id=pk)
    if request.method == 'POST':
        form = PartForm(request.POST, instance=part)
    else:
        form = PartForm(instance=part)
    return save_part_form(request,
                          form,
                          template_name='part/update.html')


@login_required()
def part_delete(request, pk):
    part = get_object_or_404(Part, id=pk)
    data = dict()
    if request.method == 'POST':
        part.delete()
        data['form_is_valid'] = True
    else:
        context = {'part': part}
        data['html_form'] = render_to_string('part/delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


@login_required()
def part_image_delete(request, pk, image_pk,slug):
    if request.method == 'POST':
        image = get_object_or_404(PartImage, id=image_pk, part=pk)
        image.img.delete()
        image.delete()
    return redirect('part-detail', pk=pk, slug=slug)


@login_required()
def part_image_upload(request, pk, slug):
    part = get_object_or_404(Part, id=pk)
    if request.method == 'POST':
        uploaded_file = request.FILES
        for file in uploaded_file:
            new_image = request.FILES[file]
            PartImage(part=part, img=new_image).save()
        return redirect('part-detail', pk=pk, slug=slug)
    return render(request, 'part/upload-image.html')


