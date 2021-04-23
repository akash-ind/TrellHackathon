from django.shortcuts import render, redirect
from trell.models import User, Trail
from django.contrib.auth import authenticate, login as user_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "trell/landing.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            user_login(request, user)
            messages.success(request, "Login Successful!!")
            return redirect('trell:profile')
        else:
            messages.warning(request, "Can't  find user")
            return redirect('trell:login')
    else:
        return render(request, 'trell/register.html')


def register(request):
    if request.method == "GET":
        return render(request, 'trell/register.html')
    else:
        posted_data = request.POST
        email = posted_data.get('email')
        if User.objects.filter(email = email).exists():
            messages.warning(request, "The user with this email already exists.Please login.")
        first_name = posted_data.get('first_name')
        last_name = posted_data.get('last_name')
        user = User(first_name = first_name, 
        last_name= last_name, email = email)
        password = posted_data.get('password')
        user.set_password(password)
        user.save()
        user_login(request, user)
        messages.success(request, "User signed up successfully")
        return redirect("trell:login")


@login_required
def profile(request):
    return render(request, 'trell/profile.html')


@login_required
def dashboard(request):
    return render(request, 'trell/dashboard.html')

from openpyxl import load_workbook
from django.conf import settings
import os


@login_required
def populate_trails(request):
    wb = load_workbook(os.path.join(settings.BASE_DIR, 'Trell.xlsx'))
    sheet = wb['Sheet1']
    for i in range(2, 103):
        id = int(float(sheet[f'A{i}'].value))
        trail = Trail(trail_id = id)
        trail.user =  request.user
        trail.save()

    return redirect('trell:dashboard')