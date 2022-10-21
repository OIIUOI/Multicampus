from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(req):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
        }
    return render(req, 'articles/index.html', context)

def create(req):
    if req.method == 'POST':
        articleform = ArticleForm(req.POST)
        if articleform.is_valid():
            savearticle = articleform.save()
            return redirect('articles:detail', savearticle.pk)
    else:
        context = {
            'articleform' : ArticleForm()
        }
    return render(req, 'articles/create.html', context)

def detail(req, pk):
    context = {
        'article' : Article.objects.get(pk=pk)
    }
    return render(req, 'articles/detail.html', context)

def update(req, pk):
    update_article = Article.objects.get(pk=pk)
    if req.method == 'POST':
        articleform = ArticleForm(req.POST, instance = update_article)
        if articleform.is_valid():
            savearticle = articleform.save()
            return redirect('articles:detail', savearticle.pk)
    else:
        context = {
            'articleform' : ArticleForm(instance = update_article)
        }
    return render(req, 'articles/update.html', context)

def delete(req, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')