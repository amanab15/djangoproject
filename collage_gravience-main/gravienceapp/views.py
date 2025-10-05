from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.conf import settings
from .forms import GrievanceForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Home Page
def viewdata(request):
    return render(request, "home.html")


# Grievance Form (login required)
@login_required
def grievance_form(request):
    if request.method == 'POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            grievance = form.save(commit=False)
            grievance.student_name = request.user.username  # assuming you store username
            grievance.save()
            messages.success(request, "Grievance submitted successfully!")
            return redirect('viewdata')  # redirect to home or a thank-you page
    else:
        form = GrievanceForm()
    return render(request, 'gravienceapp/student_grievance.html', {'form': form})


# Registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('viewdata')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout
def user_logout(request):
    logout(request)
    return redirect('login')


# Contact Page
def contact(request):
    return render(request, "contact.html")


# About Page with email sending
def about(request):
    if request.method == "POST":
        student_email = request.POST.get("email")
        message = request.POST.get("message")
        send_mail(
            subject="Student Query from Grievance System",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["teacher@example.com"],  # teacher's email
            fail_silently=False,
        )
        messages.success(request, "Email sent successfully!")
        return redirect('about')
    return render(request, "about.html")
