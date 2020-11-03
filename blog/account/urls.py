from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # path("login/", views.user_login, name="login"),
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("activate/<uidb64>/<token>/", views.activate, name="activate"),
]
