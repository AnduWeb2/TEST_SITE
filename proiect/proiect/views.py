from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

def about(request):
    return render(request, 'about.html')

def LogOut(request):
    logout(request)
    return redirect("/login")