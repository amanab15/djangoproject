from django.shortcuts import render, redirect, get_object_or_404
from .models import Grievance
from .forms import GrievanceForm

# List all grievances
def grievance_list(request):
    grievances = Grievance.objects.all()
    return render(request, 'grievance/grievance_list.html', {'grievances': grievances})

# Create a new grievance
def grievance_create(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grievance_list')
    else:
        form = GrievanceForm()
    return render(request, 'grievance/grievance_form.html', {'form': form})

# Update a grievance
def grievance_update(request, pk):
    grievance = get_object_or_404(Grievance, pk=pk)
    if request.method == 'POST':
        form = GrievanceForm(request.POST, instance=grievance)
        if form.is_valid():
            form.save()
            return redirect('grievance_list')
    else:
        form = GrievanceForm(instance=grievance)
    return render(request, 'grievance/grievance_form.html', {'form': form})

# Delete a grievance
def grievance_delete(request, pk):
    grievance = get_object_or_404(Grievance, pk=pk)
    if request.method == 'POST':
        grievance.delete()
        return redirect('grievance_list')
    return render(request, 'grievance/grievance_confirm_delete.html', {'grievance': grievance})
