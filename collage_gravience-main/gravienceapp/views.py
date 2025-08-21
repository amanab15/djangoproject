from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import GrievanceForm, CustomUserCreationForm


# Home Page / Viewdata
def viewdata(request):
    return render(request, "home.html")


# Grievance Form
def grievance_form(request):
    if request.method == "POST":
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "thankyou.html")  # simple success page
    else:
        form = GrievanceForm()
    return render(request, "grievance_form.html", {"form": form})


# ✅ Register (Sign Up)
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("student_grievance")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_grievance')  # redirect after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
