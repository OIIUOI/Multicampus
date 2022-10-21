from dataclasses import field
from .models import Article
from django import forms

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'content']