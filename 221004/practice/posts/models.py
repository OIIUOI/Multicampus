from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
