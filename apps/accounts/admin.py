from django.contrib import admin

from apps.accounts.models import Profile, Region, Country, District, User


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'country', 'phone_number', 'home_number', 'first_name']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'activate_date']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'sort_number', 'status']


class RegionAdmin(admin.ModelAdmin):
    list_display = ['country', 'name', 'code', 'sort_number', 'status']


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['country', 'region', 'name', 'code', 'sort_number', 'status']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, AccountAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
