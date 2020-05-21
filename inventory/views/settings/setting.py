from django.shortcuts import render, get_object_or_404
from inventory.models import VehicleManufacturers, Location, PartCategory
from invoice.models import CompanyDetails
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class SettingsList(LoginRequiredMixin, ListView):
    template_name = 'settings/list.html'

    def get_manufacturers(self):
        return VehicleManufacturers.objects.all()

    def get_locations(self):
        return Location.objects.all()

    def get_part_categories(self):
        return PartCategory.objects.all()

    def get_company_details(self):
        return CompanyDetails.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            'manufacturers': self.get_manufacturers(),
            'locations': self.get_locations(),
            'part_categories': self.get_part_categories(),
            'company_details': self.get_company_details(),
        }
        return render(request, self.template_name, context)
