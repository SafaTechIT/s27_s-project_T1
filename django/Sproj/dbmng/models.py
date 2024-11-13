from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class users(AbstractUser):
    image = models.ImageField(upload_to='images/', blank=True)
class tags(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class post (models.Model):
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    title = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(tags)
    image = models.ImageField(upload_to = 'images/', blank=True)
    def __str__(self):
        return self.title
class comments(models.Model):
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank=True)
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
class reply(models.Model):
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    comment = models.ForeignKey(comments, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
class massage(models.Model):
    sender = models.ForeignKey(users, on_delete=models.CASCADE)
    receiver = models.ForeignKey(users, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank=True)
    content = models.TextField(blank=True)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
class mreply(models.Model):
    author = models.ForeignKey(users, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/', blank=True)
    to = models.ForeignKey(massage, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

