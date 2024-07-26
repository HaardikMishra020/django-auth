"""
URL configuration for UserAuth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,reverse_lazy
from users import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login', permanent=False)),
    path("admin/", admin.site.urls),
     path('register/',views.register_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('profile/',views.profile_view,name="profile"),
    path('change-password/',views.changepassword_view,name="change-password"),
    path('forgot-password/',views.forgotpassword_view,name="forgot-password"),
    # path("login/", auth_views.LoginView.as_view()),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    # path("users/",include('users.urls')),
]
