from django.contrib import admin
from .models import Grievance

@admin.register(Grievance)
class GrievanceAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student_name', 'email', 'subject', 'description')
