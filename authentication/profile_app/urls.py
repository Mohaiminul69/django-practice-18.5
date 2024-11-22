from django.contrib import admin
from django.urls import path
from profile_app.views import home, sign_up, user_login, user_logout

urlpatterns = [
    path("", home, name="homepage"),
    path("sign_up/", sign_up, name="signup_page"),
    path("login/", user_login, name="login_page"),
    path("logout/", user_logout, name="logout_page"),
]
