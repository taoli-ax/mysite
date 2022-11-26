from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Reporter(models.Model):
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author}'


class Article(models.Model):
    header_line = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(Reporter, null=True, on_delete=models.SET_NULL)
    content = models.TextField()

    def __str__(self):
        return f'{self.header_line}'

    def get_absolute_url(self):
        return reverse('articledetail',kwargs={'id':self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=255)
    content_reply = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}:{self.content}'
