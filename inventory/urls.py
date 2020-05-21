from django.urls import path, include
# from .urls.parts import urlpatterns as parts_urls
# from .urls.vehicles import urlpatterns as vehicles_urls
# from .urls.settings import urlpatterns as settings_urls

from . import views


urlpatterns = [


    path('vehicles/', views.VehicleListView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>-<slug:slug>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicles/<int:pk>-<slug:slug>/update/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicles/create/', views.VehicleCreateView.as_view(), name='vehicle-create'),

    path('vehicles/<int:pk>/delete/', views.vehicle_delete, name='vehicle-delete'),

    path('vehicles/<int:pk>-<slug:slug>/upload-image/', views.vehicle_image_upload, name='vehicle-image-upload'),
    path('vehicles/<int:pk>-<slug:slug>/delete-image/<int:image_id>/', views.vehicle_image_delete, name='vehicle-image-delete'),

    path('ajax/load-models/', views.load_vehicle_model, name='ajax-load-models'),


    path('vehicles/model/', views.ModelListView.as_view(), name='vehicle-model-list'),
    path('vehicles/model/create/', views.ModelCreateView.as_view(), name='vehicle-model-create'),
    path('vehicles/model/<int:pk>-<slug:slug>/update/', views.ModelUpdateView.as_view(), name='vehicle-model-update'),
    path('vehicles/model/<int:pk>-<slug:slug>/delete/', views.model_delete, name='vehicle-model-delete'),


    path('settings/list', views.SettingsList.as_view(), name='settings-list'),

    path('settings/manufacturer/create', views.manufacturer_create, name='vehicle-manufacturer-create'),
    path('settings/manufacturer/<int:pk>/delete', views.manufacturer_delete,
         name='manufacturer-delete'),
    path('settings/manufacturer/<int:pk>/update', views.manufacturer_update,
         name='manufacturer-update'),

    path('settings/location/create', views.location_create, name='location-create'),
    path('settings/location/<int:pk>/delete', views.location_delete,
         name='location-delete'),
    path('settings/location/<int:pk>/update', views.location_update,
         name='location-update'),

    path('settings/company/<int:pk>/delete', views.company_delete,
         name='company-delete'),
    path('settings/company/<int:pk>/update', views.company_update,
         name='company-update'),


    path('settings/part/category/create', views.category_create, name='part-category-create'),
    path('settings/part/category/<int:pk>/delete', views.category_delete,
         name='part-category-delete'),
    path('settings/part/category/<int:pk>/update', views.category_update,
         name='part-category-update'),


    path('parts/export/csv/', views.part_export_to_csv, name='part-export-csv'),
    path('parts/export/json/', views.part_export_to_json, name='part-export-json'),

    path('vehicles/export/csv/', views.vehicle_export_to_csv, name='vehicle-export-csv'),
    path('vehicles/export/json/', views.vehicle_export_to_json, name='vehicle-export-json'),

    path('parts/', views.PartListView.as_view(), name='part-list'),
    path('parts/<int:pk>-<slug:slug>/', views.PartDetailView.as_view(), name='part-detail'),
    path('parts/<int:pk>/delete/', views.part_delete, name='part-delete'),
    path('parts/<int:pk>-<slug:slug>/update/', views.part_update, name='part-update'),
    path('parts/create/', views.part_create, name='part-create'),

    path('parts/<int:pk>-<slug:slug>/upload-image/', views.part_image_upload, name='part-image-upload'),
    path('parts/<int:pk>-<slug:slug>/delete-image/<int:image_pk>/', views.part_image_delete, name='part-image-delete'),

    path('parts/import', views.import_part, name='part-import'),
    path('vehicles/import', views.import_vehicle, name='vehicle-import'),

]


