from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null = True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.body[0:50]
    
        