from django import forms
from .models import Grievance

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Grievance
        fields = ['student_name', 'email', 'subject', 'description']
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
