from django.urls import path, include
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
]
