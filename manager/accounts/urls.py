from django.contrib import admin
from django.urls import path, include
from main.views import index
from . import views
from django.contrib.auth import views as auth_views
from .views import *

app_name = "accounts"

#маршрутизатор

urlpatterns = [
    path('register_user', views.register_user, name="register_user"),
    path('', include('django.contrib.auth.urls')),
    path('edit/', views.edit, name='edit'),
    path('profile/', views.show_profile, name='show_profile'),
    path('all_profiles/', views.all_profiles, name='all_profiles'),
    path('password_change/', ChangePasswordView.as_view(), name='password_change'),
]

"""path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),"""

"""path('password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),"""

