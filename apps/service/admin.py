from django.contrib import admin

from apps.service.models import Service


# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'phone_number', 'service_phone_number']
    list_display_links = ["name"]


admin.site.register(Service, ServiceAdmin)
