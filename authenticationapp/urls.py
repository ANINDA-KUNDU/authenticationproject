from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name = "home"),
    path('register', views.Register, name = "register"),
    path('login', views.Login, name = "login"),
    path('logout', views.Logout, name = "logout"),
    path('forgot-password', views.ForgotPassword, name = "forgot-password"),
    path('password-reset-sent/<str:reset_id>', views.PasswordResetSent, name = "password-reset-sent"),
    path('reset-password/<str:reset_id>', views.ResetPassword, name = "reset-password"),
]