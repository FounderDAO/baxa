from django.contrib import admin

from apps.service.models import Service, ServiceImage, Comment


# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'phone_number', 'service_phone_number']
    list_display_links = ["name"]


class ServiceImgAdmin(admin.ModelAdmin):
    list_display = ["service", "file", "status", "sort_number"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["parent", "user", "description", "rank"]


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImgAdmin)
admin.site.register(Comment, CommentAdmin)
