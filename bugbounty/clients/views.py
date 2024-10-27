from .forms import UserRegistration,UserLoginForm
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login
def User_registration(request):
    if request.method=='POST':
        form=UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form=UserRegistration()
    return render(request,'client_signup.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            print(username)
            print(password)
            print(user)
            if user is not None:
                login(request,user)
                return redirect('user_dashboard')
            else:
                form.add_error(None,"invalid username or password")
    else:
        form=UserLoginForm()
    return render(request,'user_login.html',{'form':form})
@login_required
def user_dashboard(request):
    if request.method=='GET':
        return render(request,'user_dashboard.html')
