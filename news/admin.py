from django.contrib import admin
from .models import Article,Reporter,Comment
# Register your models here.
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(Comment)
