from django.contrib import admin
from .models import Grievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ("id", "student_name", "email", "subject", "description", "created_at")
