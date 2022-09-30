from django.contrib import admin

from apps.accounts.models import Profile, Region, Country, District


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'phone_number', 'home_number', 'first_name']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'sort_number', 'status']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['country', 'name', 'code', 'sort_number', 'status']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['country', 'region', 'name', 'code', 'sort_number', 'status']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
