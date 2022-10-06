from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    return render(request, "posts/index.html")


def create(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            savepost = postform.save()
            return redirect("posts:detail", savepost.pk)
    else:
        postform = PostForm()
    context = {"Postform": postform}
    return render(request, "posts/create.html", context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/detail.html", {"post": post})


def delete(request):
    pass


def update(request):
    pass
