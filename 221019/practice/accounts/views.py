from django.shortcuts import render
from .forms import CustomUserForm

# Create your views here.
# def signup(request):
def signup(request):
    if request.method == 'POST':
        user_form = CustomUserForm(request.)
