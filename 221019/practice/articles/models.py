from django.db import models
from ..pjt.settings import AUTH_USER_MODEL

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 35)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)