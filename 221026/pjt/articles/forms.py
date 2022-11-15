from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class Comment(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']