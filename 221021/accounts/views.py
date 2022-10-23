from django.shortcuts import render, redirect
from .forms import CustomUserForm
from django.contrib.auth import get_user_model, login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(req):
    if req.method == 'POST':
        userform = CustomUserForm(req.POST)
        if userform.is_valid():
            saveuser = userform.save()
            return redirect('accounts:profile', saveuser.pk)
    else:
        userform = CustomUserForm()
    context = {
        'userform' :userform
        }
    return render(req, 'accounts/signup.html', context)

def profile(req, pk):
    context = {
        'user' : get_user_model().objects.get(pk=pk)
        }
    return render(req, 'accounts/profile.html', context)

def log_in(req):
    if req.method == 'POST':
        loginform = AuthenticationForm(req, data=req.POST)
        if loginform.is_valid():
            login(req, loginform.get_user())
            return redirect('articles:index')
            
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform' : loginform
        }
    return render(req, 'accounts/login.html', context)