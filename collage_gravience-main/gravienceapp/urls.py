from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('viewdata/', views.viewdata, name='viewdata'),
    path('student-grievance/', views.grievance_form, name='student_grievance'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
