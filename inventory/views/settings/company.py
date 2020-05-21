from django.http import JsonResponse
from django.template.loader import render_to_string
from invoice.models import CompanyDetails
from invoice.forms import CompanyDetailsForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required()
def save_company_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['company_details'] = render_to_string('settings/company/list.html', {
                'company': CompanyDetails.objects.all()
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
def company_create(request):
    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST, request.FILES)
    else:
        form = CompanyDetailsForm()
    return save_company_form(request, form, 'settings/company/create.html')

@login_required()
def company_update(request, pk):

    company = get_object_or_404(CompanyDetails, pk=pk)
    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST, instance=company, files=request.FILES)
    else:
        form = CompanyDetailsForm(instance=company)
    return save_company_form(request,
                             form,
                             'settings/company/update.html')

@login_required()
def company_delete(request, pk):
    company = get_object_or_404(CompanyDetails, pk=pk)
    data = dict()
    if request.method == 'POST':
        company.delete()
        data['form_is_valid'] = True
        data['company_list'] = render_to_string('settings/company/list.html', {
            'company': CompanyDetails.objects.all()
        })
    else:
        context = {'company': company}
        data['html_form'] = render_to_string('settings/company/delete.html',
                                             context,
                                             request=request,
                                             )
    return JsonResponse(data)
