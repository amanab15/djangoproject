from django.db import models
from django.contrib.auth.models import User  # Optional: to link grievances to users

class Grievance(models.Model):
    # Optional: Link grievance to logged-in user
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return f"{self.student_name} - {self.subject}"
