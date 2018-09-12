from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserInfo, RegisterForm, EditProfileForm
from .models import Info


def index(request):
    return render(request, 'user/blood.html')

def user_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.')
            return redirect('index')
        else:
            messages.success(request, 'Username or password is invalid.')
            return redirect('login')
    return render(request, 'user/login.html', {})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out')
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully.')
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user/change_password.html', {'form':form})

def profile(request):
    return render(request, 'user/profile.html', {})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editing Done.')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'user/edit_profile.html', {'form':form})

def forgotten_password(request):
    return render(request, 'user/forgotten_password.html', {})

def blood_donors(request):
    info = Info.objects.all()
    return render(request, 'user/blood donors.html', {'info': info})


def donate_blood(request):
    if request.method == 'POST':
        form = UserInfo(request.POST)
        if form.is_valid():
            new_user = Info(name=request.POST['name'], age=request.POST['age'], email=request.POST['email'],
                        address=request.POST['address'], contact_number=request.POST['contact_number'],
                        blood_group=request.POST['blood_group'])
            new_user.save()
            return redirect('index')
    else:
        form = UserInfo()

    return render(request, 'user/donate blood.html', {'form': form})


def about(request):
    return render(request, 'user/about.html')
