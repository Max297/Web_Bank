from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from profiles.models import Status 
import random

def randomGen():
    # return a 6 digit random number
    return int(random.uniform(100000, 999999))

def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # getting details of current user
    except:
        # if no details exist (new user), create new details
        curr_user = Status()
        curr_user.account_number = randomGen() # random account number for every new user
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "profiles/profile.html", {"curr_user": curr_user})

def money_transfer(request):
    return render (request,"profiles/money_transfer.html")

def loan(request):
    return render(request, "profiles/loans.html")



def online_pay(request):
    return render(request, "profiles/online_payment.html")

def settings(request):
    return render(request, "profiles/settings.html")


def delete_account(request):
    return render(request, "profiles/delete_account.html")
