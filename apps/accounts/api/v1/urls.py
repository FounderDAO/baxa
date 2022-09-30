from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('country/create/', views.CountryCreateView),
    path('country/edit/<int:id>/', views.CountryEditingView),
    path('country/delete/<int:id>/', views.CountryCreateView),
    path('region/create/', views.RegionCreateView),
    path('region/edit/<int:id>/', views.RegionEditView),
    path('region/delete/<int:id>/', views.RegionCreateView),
    path('district/create/', views.DistrictCreateView),
    path('district/edit/<int:id>/', views.DistrictEditView),
    path('district/delete/<int:id>/', views.DistrictCreateView)
]
