from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm
from .forms import Comment as CommentForm
# Create your views here.

def index(req):
    articles = Article.objects.all()
    cxt = {'articles' : articles}
    return render(req, 'articles/index.html', cxt)

def create(req):
    if req.method == 'POST':
        articleform = ArticleForm(req.POST)
        if articleform.is_valid():
            savearticle = articleform.save()
            return redirect('articles:detail', savearticle.pk)
    else:
        articleform = ArticleForm()
    cxt = {
        'articleform' : articleform
    }
    return render(req, 'articles/create.html', cxt)

def detail(req, pk):
    article = Article.objects.get(pk=pk)
    cxt = {
        'article' : article,
        'comments' : article.comment_set.all(),
        }
    return render(req, 'articles/detail.html', cxt)
