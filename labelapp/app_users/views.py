# app_users/views.py

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .form import RegisterForm  

# Create your views here.

def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print("Ok It's right")
            return HttpResponseRedirect(reverse("home"))
    else:
        print("It's not Ok")
        form = RegisterForm()
    # GET
    context = {"form": form}
    return render(request, "app_users/register.html", context)


