from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def new(request):
    return render(request, "posts/new.html")


def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    return redirect("posts:index")
