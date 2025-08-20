from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('viewdata/', views.viewdata),
    path('admin/', views.viewdata),
    path('student-grievance/', views.grievance_form, name="student_grievance"),
]
