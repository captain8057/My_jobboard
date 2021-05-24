from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = RichTextUploadingField(config_name="custom")
    date_posted = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True,null=True)
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