from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "home.html")


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User registered Successfully")
    else:
        form = RegistrationForm()
    return render(request, "sign_up.html", {"form": form})
