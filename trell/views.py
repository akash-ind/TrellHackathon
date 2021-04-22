from django.shortcuts import render
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
        return render(request, 'trell/login.html')