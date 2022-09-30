from django.urls import path, include

urlpatterns = [
    path('', include('apps.service.api.urls'))
]
