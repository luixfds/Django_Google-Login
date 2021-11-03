from django.contrib import auth
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'home/home.html')


def login(request):
    return render(request, 'home/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')