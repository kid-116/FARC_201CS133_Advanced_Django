from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import AccountAuthenticationForm, AccountSignupForm

def signup_acc(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method == 'POST':
        form = AccountSignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('sections:home_path')
    else:
        form = AccountSignupForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_acc(request):
    user = request.user
    if user.is_authenticated:
        return redirect('sections:home_path')
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return redirect('sections:home_path')
    else:
        form = AccountAuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_acc(request):
    logout(request)
    return redirect('landing_path')
