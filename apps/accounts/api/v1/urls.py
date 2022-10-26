from django.urls import path

from . import views

urlpatterns = [
    path('country/list/', views.CountryList.as_view()),
    path('country/<int:pk>/', views.CountryDetail.as_view()),
    path('region/list/', views.RegionList.as_view()),
    path('region/<int:pk>/', views.RegionDetail.as_view()),
    path('district/list/', views.DistrictList.as_view()),
    path('district/<int:pk>/', views.DistrictDetail.as_view()),
    path('account/list/', views.AccountList.as_view()),
    path('account/<int:pk>/', views.AccountDetail.as_view()),
    path('profile/list/', views.ProfileCreateView.as_view()),
    path('profile/<int:pk>/', views.ProfileDetail.as_view()),
]
