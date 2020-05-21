from django.contrib import admin
from user.models import SecurityCode
from user.forms import SecurityCodeForm
# Register your models here.



class SecurityCodeAdmin(admin.ModelAdmin):

    form = SecurityCodeForm
    list_display = ['code']

admin.site.register(SecurityCode, SecurityCodeAdmin)


