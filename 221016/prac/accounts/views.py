from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)


def detail(request, pk):
    
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user
    }
    return render(request,'accounts/detail.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # if request.GET.get('next'):
            #     return redirect(request.Get.get('next'))
            # else:
            #       return render(request,'accounts/else.html')
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context={
        'form' : form
    }
    return render(request,'accounts/login.html', context)

def elses(request):
    return render(request,'accounts/else.html')


def logout(request):
    auth_logout(request)
    return redirect('accounts:else')
