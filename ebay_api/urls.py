from django.urls import path
from .views import (
    AccountListView,
    AccountBeginCreateView,
    AccountRejectCreateView,
    AccountFinishCreateView,
    AccountDetailView,
    AccountUpdateView,
    AccountDeleteView,
    PrivacyPolicyView,
)

APP_NAME = 'ebay_api'

urlpatterns = [
    path(
        '',
        AccountListView.as_view(),
        name=APP_NAME + '_account_list',
    ),
    path(
        'begin_create/',
        AccountBeginCreateView.as_view(),
        name=APP_NAME + '_account_begin_create',
    ),
    path(
        'reject_create/',
        AccountRejectCreateView.as_view(),
        name=APP_NAME + '_account_reject_create',
    ),
    path(
        'finish_create/',
        AccountFinishCreateView.as_view(),
        name=APP_NAME + '_account_finish_create',
    ),
    path(
        'privacy_policy/',
        PrivacyPolicyView.as_view(),
        name=APP_NAME + '_privacy_policy',
    ),
    path(
        '<int:pk>/',
        AccountDetailView.as_view(),
        name=APP_NAME + '_account_detail',
    ),
    path(
        '<int:pk>/update/',
        AccountUpdateView.as_view(),
        name=APP_NAME + '_account_update',
    ),
    path(
        '<int:pk>/delete/',
        AccountDeleteView.as_view(),
        name=APP_NAME + '_account_delete',
    ),
]