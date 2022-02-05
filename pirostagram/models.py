from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=100)
  image = models.ImageField(upload_to="image/", null=True, blank=True)
  content = models.CharField(max_length=2000)
  likes = models.IntegerField(null=True, blank=True)

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  comment = models.CharField(max_length=200)