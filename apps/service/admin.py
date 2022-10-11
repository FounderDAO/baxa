from django.contrib import admin

from apps.service.models import Service, ServiceImage, Comment, Category


# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'id', 'description', 'phone_number', 'service_phone_number']
    list_display_links = ["name"]


class ServiceImgAdmin(admin.ModelAdmin):
    list_display = ["service", "file", "status", "sort_number"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["parent", "user", "description", "rank", "status"]
    list_display_links = ['user']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["parent", "name", "description", "sort_number"]
    list_display_links = ['name']


admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceImage, ServiceImgAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
