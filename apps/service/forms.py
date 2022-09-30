from django.contrib.auth.forms import UserChangeForm

from apps.service.models import Service


class CustomServiceForm(UserChangeForm):
    class Meta:
        model = Service
        fields = ('name', 'description', 'phone_number', 'address', 'service_phone_number', 'is_premium')