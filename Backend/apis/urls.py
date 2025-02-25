from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView, PasswordResetView,LogoutView,TokenRefreshView

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/password-reset/", PasswordResetView.as_view(), name="password-reset"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
