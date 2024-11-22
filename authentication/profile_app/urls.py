from django.contrib import admin
from django.urls import path
from profile_app.views import home

urlpatterns = [
    path("", home, name="homepage"),
]
