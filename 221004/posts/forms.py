from socket import fromshare
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        # 타이틀만 필요하다면 타이틀만 써도 됨
        # ['title'] 이렇게! or ['title', 'content']