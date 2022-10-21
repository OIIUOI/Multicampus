from django.shortcuts import render

# Create your views here.
app_name = "todos"


def index(request):
    return render(request, "index.html")
