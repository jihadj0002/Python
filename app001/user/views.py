from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

# Create your views here.
def user(request):
    return render(request, "user/main.html")

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password =form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect('user')
    else:
        form = LoginForm()

    return render(request, "user/login.html", {
        'form': form
    } )

def reg(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    return render(request, "user/signup.html", {
        'form': form
    })