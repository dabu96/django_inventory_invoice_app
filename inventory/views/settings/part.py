from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse

from ...models import PartCategory
from ...forms import PartCategoryForm
from django.contrib.auth.decorators import login_required


@login_required()
def save_part_category_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            data['part_category_list'] = render_to_string('settings/part_category/list.html', {
                'part_categories': PartCategory.objects.all()
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
def category_create(request):
    if request.method == 'POST':
        form = PartCategoryForm(request.POST)
    else:
        form = PartCategoryForm()
    return save_part_category_form(request, form, 'settings/part_category/create.html')


@login_required()
def category_update(request, pk):
    category = get_object_or_404(PartCategory, pk=pk)
    if request.method == 'POST':
        form = PartCategoryForm(request.POST, instance=category)
    else:
        form = PartCategoryForm(instance=category)
    return save_part_category_form(request,
                                  form,
                                  'settings/part_category/update.html')


@login_required()
def category_delete(request, pk):
    category = get_object_or_404(PartCategory, pk=pk)

    data = dict()
    # try:
    if request.method == 'POST':
        category.delete()
        data['form_is_valid'] = True
        categories = PartCategory.objects.all()
        data['part_category_list'] = render_to_string('settings/part_category/list.html', {
            'category': categories
        })
    else:
        context = {'category': category}
        data['html_form'] = render_to_string('settings/part_category/delete.html',
                                                     context,
                                                     request=request,
                                                     )
    return JsonResponse(data)
