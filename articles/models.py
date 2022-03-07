from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    contenst = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
