from django.urls import path
from . import views

urlpatterns = [
    path('', views.grievance_list, name='grievance_list'),
    path('create/', views.grievance_create, name='grievance_create'),
    path('update/<int:pk>/', views.grievance_update, name='grievance_update'),
    path('delete/<int:pk>/', views.grievance_delete, name='grievance_delete'),
]
