import django_tables2 as tables
from .models import VehicleOwnership, Part


class VehicleTable(tables.Table):
    select = tables.TemplateColumn('<input class="selectCheck" type="checkbox" value="{{ record.pk }}" />',
                                   verbose_name="Select")

    vehicle_model__manufacturer = tables.Column()
    vehicle_model = tables.Column(linkify=('vehicle-detail', {'pk': tables.A('pk'), 'slug': tables.A('slug')}))
    vehicle_model__year = tables.Column()
    vehicle_model__litre = tables.Column()
    colour = tables.Column()
    location = tables.Column()

    editHTML = '<button type="button" class="btn btn-warning btn-sm js-update-vehicle"  data-url="{% url ' \
               '"vehicle-update" ' \
               'record.id record.slug %}"><i class="fa  fa-pencil"></i>  Update</button> '

    edit = tables.TemplateColumn(editHTML)





class VehiclePartsTable(tables.Table):
    name = tables.Column(verbose_name='Part', linkify=('part-detail', {'pk': tables.A('pk'), 'slug': tables.A('slug')}))
    vehicle = tables.Column(linkify=('vehicle-detail', {'pk': tables.A('vehicle_id'),
                                                        'slug': tables.A('vehicle__slug')}))
    category = tables.Column()
    selling_price = tables.Column()

    # class Meta:
    #     model = Part


class VehicleModelTable(tables.Table):
    select = tables.TemplateColumn('<input class="selectCheck" type="checkbox" value="{{ record.pk }}" />',
                                   verbose_name="Select")
    name = tables.Column()
    manufacturer = tables.Column()
    year = tables.Column()
    litre = tables.Column()
    transmission = tables.Column()
    vehicle_type = tables.Column()

    editHTML = '<button type="button" class="btn btn-warning btn-sm js-update-vehicle-model"' \
               '  data-url="{% url "vehicle-model-update" record.id record.slug %}">' \
               '<i class="fa  fa-pencil"></i>  Update</button> '
    deleteHTML = '<button type="button" class="btn btn-danger btn-sm js-delete-vehicle-model" ' \
                 'data-url="{% url "vehicle-model-delete" record.id record.slug %}"><i class="fa  fa-trash-o"></i>' \
                 'Delete</button> '


    edit = tables.TemplateColumn(editHTML)
    delete = tables.TemplateColumn(deleteHTML)



class PartTable(tables.Table):

    select = tables.TemplateColumn('<input class="selectCheck" type="checkbox" value="{{ record.pk }}" name="{{record.name}}"/>',
                                   verbose_name="Select", orderable=False)


    name = tables.Column(verbose_name='Part', linkify=('part-detail', {'pk': tables.A('pk'), 'slug': tables.A('slug')}))
    side = tables.Column()
    vehicle = tables.Column(linkify=('vehicle-detail', {'pk': tables.A('vehicle_id'),
                                                        'slug': tables.A('vehicle__slug')}))

    category = tables.Column()
    selling_price = tables.Column()
    available = tables.Column()

    editHTML = '<button type="button" class="btn btn-warning btn-sm js-update-part"  data-url="{% url "part-update" ' \
               'record.id record.slug %}"><i class="fa  fa-pencil"></i>  Update</button> '


    edit = tables.TemplateColumn(editHTML)

    # class Meta:
    #     model = Part
    #     attrs = {"class": "paleblue"}
