from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .forms import NewUserForm, EmailOrUsernameAuthenticationForm
from django.contrib import messages




# Create your views here.

def register_view(request):
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('dashboard')
    else:      
        form=NewUserForm()
    return render(request,'users/register.html',{"form":form})


def login_view(request):
    if request.method=='POST':
        form = EmailOrUsernameAuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("dashboard")

    else:
        form = EmailOrUsernameAuthenticationForm()
    return render(request,'users/login.html',{"form":form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    user=request.user
    return render(request,'users/dashboard.html',{"data":user})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect("login")

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    user=request.user
    return render(request,'users/profile.html',{"data":user})

def changepassword_view(request):
     if not request.user.is_authenticated:
        return redirect("login")
     else:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect("dashboard")


        else:
            form=PasswordChangeForm(request.user)
        return render(request,'users/changepassword.html',{"form":form}) 

def forgotpassword_view(request):
    return render(request,'users/forgotpassword.html')