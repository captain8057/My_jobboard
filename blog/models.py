from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="blog-img/" ,null=True , default="blog-img/blog-def-img.png")
    Hyper_Text= models.TextField(blank=True)
    tags = models.ManyToManyField("Tag")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-list')



class Tag(models.Model):
    name = models.CharField(max_length=190, null=True)

    def __str__(self):
       return self.name