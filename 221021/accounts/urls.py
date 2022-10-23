from django.contrib import admin
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name = 'signup' ),
    path('profile/<int:pk>', views.profile, name = 'profile'),
    path('login/', views.log_in, name = 'login'),
]
