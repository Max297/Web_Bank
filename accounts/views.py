from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
import time
from CentralBank import settings

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:signin")
    else:
        form = UserCreationForm()
    return render(request, "accounts/create_account.html", {"form": form})

def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            settings.time_out=0.5
            return redirect("profiles:account")
        else :
            time.sleep(settings.time_out)
            settings.time_out=settings.time_out*2
            return render(request, "accounts/sign_in_repeat.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "accounts/sign_in.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("accounts:signin")
