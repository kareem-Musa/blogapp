from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title
