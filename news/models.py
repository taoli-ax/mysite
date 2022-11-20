from django.db import models


# Create your models here.

class Reporter(models.Model):

    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.author}'


class Article(models.Model):
    header_line = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(Reporter,null=True,on_delete=models.SET_NULL)
    content = models.TextField()

    def __str__(self):
        return f'{self.header_line}'
