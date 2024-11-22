from django.contrib import admin
from django.urls import path
from profile_app.views import home, sign_up

urlpatterns = [
    path("", home, name="homepage"),
    path("sign_up", sign_up, name="signup_page"),
]
