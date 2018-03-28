from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #Thumbnail and author will be added later

    #to display string version of object and not the object in the interactive shell and admin section
    def __str__(self):
        return self.title