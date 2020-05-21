from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .filters import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
import datetime
from django.core import serializers
from django.contrib import messages

from django.http import HttpResponse
from django.views.generic import View

from invoice.utils import render_to_pdf
from django.db import transaction

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import ModelMultipleChoiceField

now = datetime.datetime.now()


class InvoiceObjectMixin(object):
    model = Invoice

    def get_invoice_object(self):
        pk = self.kwargs.get('pk')
        slug = self.kwargs.get('slug')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=pk, slug=slug)
        return obj


class GeneratePdf(LoginRequiredMixin, InvoiceObjectMixin, View):
    company, created = CompanyDetails.objects.get_or_create(id=1)

    def get(self, request, *args, **kwargs):
        parts = PartBought.objects.filter(invoice=self.get_invoice_object())
        data = {
            'invoice': self.get_invoice_object(),
            'parts': parts,
            'company': self.company,
        }
        pdf = render_to_pdf('invoice/pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class InvoiceView(LoginRequiredMixin, ListView):
    template_name = 'invoice/list.html'
    queryset = Invoice.objects.all()

    def get_filter(self):
        invoice_filter = InvoiceFilter(self.request.GET, queryset=self.queryset)
        return invoice_filter

    def get_related_objects(self):
        invoices = self.get_queryset()
        parts = PartBought.objects.all()
        dict = {}
        for invoice in invoices:
            parts_bought = parts.filter(invoice=invoice)
            dict[invoice] = parts_bought
        return dict

    def get_queryset(self):
        return self.get_filter().qs

    def get(self, request, *args, **kwargs):
        invoices = self.get_related_objects()
        context = {
            'invoice_filter': self.get_filter(),
            'invoices': invoices
        }
        return render(request, self.template_name, context)


@login_required()
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    customer = get_object_or_404(Customer, id=invoice.customer.pk)
    data = dict()
    if request.method == 'POST':
        customer.delete()
        data['form_is_valid'] = True
    else:
        context = {'invoice': invoice}
        data['html_form'] = render_to_string('invoice/delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


@login_required()
def invoice_refund(request, pk):
    invoice = get_object_or_404(Invoice, id=pk)
    parts_to_refund = PartsToRefund(invoice=invoice)
    data = dict()

    if request.method == 'POST':
        with transaction.atomic():
            invoice.refunded = True
            invoice.save()
            selected_parts = request.POST.getlist('parts_select')
            for selected_part in selected_parts:
                part = get_object_or_404(Part, id=selected_part)
                part.available = True
                part.save()
        data['form_is_valid'] = True
    else:
        context = {'invoice': invoice,
                   'parts_select': parts_to_refund
                   }
        data['html_form'] = render_to_string('invoice/refund.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)


class InvoiceCreate(LoginRequiredMixin, CreateView):
    template_name = 'invoice/create.html'
    form_class = CustomerForm
    queryset = Invoice.objects.all()
    invoice = Invoice()
    customer = Customer()

    def get_params(self):
        id_string = self.request.GET.get('id')
        if id_string is not None:
            ids = [int(id) for id in id_string.split(',')]
            return ids

    def get_success_url(self):
        self.success_url = '/invoice/'
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(InvoiceCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['customer_form'] = CustomerForm(self.request.POST)
            context['invoice_formset'] = InvoiceFormSet(self.request.POST)
            context['part_bought_formset'] = PartBoughtFormSet(self.request.POST)

        else:
            part_bought_formset = PartBoughtFormSet()
            available_parts = Part.objects.filter(available=True)
            for form in part_bought_formset:
                form.fields['part'].queryset = available_parts
            manufacturers = VehicleManufacturers.objects.all()
            context['customer_form'] = CustomerForm()
            context['invoice_formset'] = InvoiceFormSet()
            context['part_bought_formset'] = part_bought_formset
            context['manufacturers'] = manufacturers
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        invoice_formset = context['invoice_formset']
        customer_form = context['customer_form']
        part_bought_formset = context['part_bought_formset']

        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()

            if invoice_formset.is_valid() and customer_form.is_valid() and part_bought_formset.is_valid():

                customer = form.save(commit=False)
                invoice = invoice_formset.save(commit=False)
                customer.instance = self.object
                customer.created_by = self.request.user
                customer.save()
                temp = part_bought_formset.save(commit=False)
                running_total = 0

                for data in invoice_formset.cleaned_data:
                    invoice = Invoice(customer=self.object, date_created=now,
                                      delivery=data.get('delivery'), reference=data.get('reference'),
                                      total_cost=running_total,
                                      sale_tax_percent=data.get('sale_tax_percent')
                                      )
                    invoice.save()
                for parts in part_bought_formset:
                    get_part = parts.cleaned_data['part']
                    part = get_object_or_404(Part, pk=get_part.pk)
                    part.available = False
                    part.save()
                    running_total += part.selling_price
                    temp = PartBought(customer=self.object, part=part, invoice=invoice)
                    temp.save()

                invoice.total_cost = running_total + invoice.delivery
                added_vat = (running_total * invoice.sale_tax_percent) / 100
                invoice.total_cost_inc_vat = invoice.total_cost + added_vat
                invoice.save()

            else:
                print('form not valid')
        return super(InvoiceCreate, self).form_valid(form)


def load_vehicle_models_for_invoice(self):
    data = dict()
    try:
        manufacturer = self.GET.get('manufacturer')
        vehicle_models = VehicleOwnership.objects.filter(manufacturer__name=manufacturer)
        models_as_json = serializers.serialize('json', vehicle_models)
        data['vehicle_models'] = models_as_json
    except Exception as e:
        data['error'] = messages.error(self.request, "Error finding manufacturer ")
    return JsonResponse(data)


def load_parts_for_invoice(self):
    data = dict()
    try:
        vehicles = self.GET.get('model')
        parts = Part.objects.filter(vehicle=vehicles, available=True)
        parts_as_json = serializers.serialize('json', parts)
        data['parts'] = parts_as_json
    except Exception as e:
        data['error'] = messages.error(self.request, "Error finding model")
    return JsonResponse(data)
