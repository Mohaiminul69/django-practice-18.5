from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, "home.html")


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered Successfully")
            return redirect("login_page")
    else:
        form = RegistrationForm()
    return render(request, "sign_up.html", {"form": form, "type": "Registration"})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "Logged In Successfully")
                login(request, user)
                return redirect("profile_page")
            else:
                messages.warning(request, "Login information is not valid")
                return redirect("signup_page")
    else:
        form = AuthenticationForm()
    return render(request, "sign_up.html", {"form": form, "type": "Login"})


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("homepage")


@login_required
def profile(request):
    return render(request, "profile.html")
