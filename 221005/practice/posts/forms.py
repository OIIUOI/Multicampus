from socket import fromshare
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class meta:
        model = Post
        field = "__all__"
