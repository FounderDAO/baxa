from django.urls import path

from apps.accounts import views

urlpatterns = [
    path('country/create/', views.CountryCreateView.as_view()),
    path('country/edit/<int:id>/', views.CountryEditingView.as_view()),
    path('country/delete/<int:id>/', views.CountryCreateView.as_view()),
    path('region/create/', views.RegionCreateView.as_view()),
    path('region/edit/<int:id>/', views.RegionEditView.as_view()),
    path('region/delete/<int:id>/', views.RegionCreateView.as_view()),
    path('district/create/', views.DistrictCreateView.as_view()),
    path('district/edit/<int:id>/', views.DistrictEditView.as_view()),
    path('district/delete/<int:id>/', views.DistrictCreateView.as_view())
]
