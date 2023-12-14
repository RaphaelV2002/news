# blog/models.py
from django.db import models
from django.contrib.auth.models import User


class BlogManager(models.Manager):
    def new(self):
        return self.order_by("-added_at")


class NewManager(models.Manager):
    def new(self):
        return self.order_by("-added_at")


class Blog(models.Model):
    objects = BlogManager()
    title = models.CharField(max_length=50)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class New(models.Model):
    objects = NewManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to="media/images")
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="new")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
