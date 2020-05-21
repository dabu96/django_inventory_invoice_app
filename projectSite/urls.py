from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static

from user import views as user_view
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from ebay_api import views as ebay_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('inventory/', include('inventory.urls')),

    path('ebay/', include('ebay_api.urls')),
    path('invoice/', include('invoice.urls')),

    # path('user/', include('users.urls')),
    path('register/', user_view.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_view.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
