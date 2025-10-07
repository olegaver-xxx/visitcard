from django.contrib.auth.models import AbstractUser
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from ckeditor.fields import RichTextField

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField('post content')
    pub_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-pub_date']


class ImageModel(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = ThumbnailerImageField(upload_to='images/', blank=True, null=True)
    index = models.PositiveIntegerField(default=0, blank=True)
    def __str__(self):
        return self.post.title
