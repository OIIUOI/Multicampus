from django.shortcuts import render,redirect
from .models import Post
import datetime
from .forms import PostForm

# Create your views here.
def index(request):
    articles = Post.objects.order_by('-pk')
    return render(request, 'posts/index.html',{'articles':articles})

def new(request):
    post_form = PostForm()
    context ={'post_form' : post_form }
    return render(request, 'posts/new.html', context)

def create(request):
    if request.method =='POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:index')
    else:
        post_form = PostForm()
    
    context = {
        'post_form' : post_form
    }
    return render(request, 'posts/new.html',)
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # savepost = Post.objects.create(title=title, content=content)
    

def detail(request, pk):
    article = Post.objects.get(pk=pk)
    return render(request, 'posts/detail.html', {'article':article})


def delete(request, pk):
    Post.objects.get(pk = pk).delete()
    return redirect('posts:index')

def edit(request, pk):
    editpost = Post.objects.get(pk=pk)
    return render(request,'posts/edit.html', {'editpost':editpost})

def update(request, pk):
    updatepost = Post.objects.get(pk=pk)
    updatepost.title = request.GET.get('title')
    updatepost.content = request.GET.get('content')
    updatepost.update_at = datetime.datetime.now()
    updatepost.save()
    return redirect('posts:index')