from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    #body = models.TextField()
    body = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    # author will be added later
    

    # to display string version of object and not the object in the interactive shell and admin section
    def __str__(self):
        return self.title

    def snippet(self):
        # return first 50 chars
        return self.body[:100] + '...'
