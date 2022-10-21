from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    context = {'articles' : Article.objects.order_by('-pk')}
    return render(request, 'articles/index.html' ,context)

def create(request):
    if request.method == 'POST':
        article = ArticleForm(request.POST)
        context = {
            'article' : article
        }
        if article.is_valid():
            article.save()
            return redirect('articles:index')
    else:
        context = {
            'articleform' : ArticleForm()
            }
    return render(request, 'articles/create.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': 
        articleform = ArticleForm(request.POST, instance = article)
        if articleform.is_valid():
            articleform.save()
            return redirect('articles:index')
    else:
        context = {
            'articleform' : ArticleForm(instance=article)
        }
    return render(request, 'articles/update.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render (request, 'articles/detail.html', {'article' : article})