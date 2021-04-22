from django.shortcuts import render, redirect
from trell.models import User
from django.contrib.auth import authenticate, login as user_login
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            user_login(request, user)
            messages.success(request, "Login Successful!!")
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