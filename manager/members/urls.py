from django.contrib import admin
from django.urls import path, include
from main.views import index
from . import views
from django.contrib.auth import views as auth_views

app_name = "members"

#маршрутизатор

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
