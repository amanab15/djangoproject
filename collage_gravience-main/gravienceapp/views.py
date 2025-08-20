from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GrievanceForm


def viewdata(request):
    # students = students.objects.all() 
    return render(request,"home.html")                   

def grievance_form(request):
    if request.method == "POST":
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html")  # make a simple success page
    else:
        form = GrievanceForm()
    return render(request, "grievance_form.html", {"form": form})
