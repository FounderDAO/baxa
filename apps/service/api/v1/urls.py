from django.urls import path
from . import views

urlpatterns = [
    path('service/create/', views.ServiceCreateView.as_view()),
    path('service/edit/<int:id>/', views.ServiceEditView.as_view()),
    path('service/delete/<int:id>/', views.ServiceDeleteView.as_view()),
    path('service/detail/<int:id>/', views.ServiceDetailView.as_view()),
    path('service/all/', views.ServiceView.as_view()),
    path('comment/create/', views.CommentCreateView.as_view()),
    path('comment/edit/<int:id>/', views.CommentEditView.as_view()),
    path('comment/delete/<int:id>/', views.CommentDeleteView.as_view()),
    path('category/create/', views.CategoryCreateView.as_view()),
    path('category/delete/<int:id>/', views.CategoryCreateView.as_view()),
    path('category/edit/<int:id>/', views.CategoryEdit.as_view()),
    path('category/list/', views.CategoryEdit.as_view())
]
