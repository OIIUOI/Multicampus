from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            auth_login(request, user)  
            return redirect('articles:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.')
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def folloow(req, pk):
    user = get_user_model().objects.get(pk=pk)
    if req.user in user.following.all():
        user.following.remove(req.user)
    else:
        user.following.add(req.user)
    return redirect('accounts:detail', pk)



# def follow(request, pk):
#     # 프로필에 해당하는 유저를 로그인한 유저가!
#     user = get_user_model().objects.get(pk=pk)
#     if request.user == user:
#         messages.warning(request, '스스로 팔로우 할 수 없습니다.')
#         return redirect('accounts:detail', pk)
#     if request.user in user.followers.all():
#     # (이미) 팔로우 상태이면, '팔로우 취소'버튼을 누르면 삭제 (remove)
#         user.followers.remove(request.user)
#     else:
#     # 팔로우 상태가 아니면, '팔로우'를 누르면 추가 (add)
#         user.followers.add(request.user)
#     return redirect('accounts:detail', pk)
