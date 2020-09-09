from django.db import models
from Postapp.models import Post
# Create your models here.

class Tag(models.Model):
    tagname=models.TextField()
    tagsforpost=models.ManyToManyField(Post)

    def __str__(self):
        return self.tagname