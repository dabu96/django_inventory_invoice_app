from django.urls import path, re_path
from . import views



urlpatterns = [
    path('', views.InvoiceView.as_view(), name='invoice-list'),
    # path('<int:pk>-<slug:slug>/', views.InvoiceDetailView.as_view(), name='invoice-detail'),

    path('<int:pk>/delete', views.invoice_delete, name='invoice-delete'),

    path('create/', views.InvoiceCreate.as_view(), name='invoice-create'),
    path('<int:pk>-<slug:slug>/pdf/', views.GeneratePdf.as_view(), name='invoice-pdf'),

    path('<int:pk>/refund/', views.invoice_refund, name='invoice-refund'),

    path('load-ajax-models/', views.load_vehicle_models_for_invoice, name='load-vehicle-models-for-invoice'),
    path('load-ajax-parts/', views.load_parts_for_invoice, name='load-parts-for-invoice')

]

