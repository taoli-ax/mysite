from django.shortcuts import render
from .models import Article, Reporter
from django.views import generic


# Create your views here.
def index(request):
    context={'msg':' Hello World! '}
    return render(request,'news/index.html',context)


class ArticleListView(generic.ListView):
        model=Article
        queryset=Article.objects.filter(header_line__isnull=False)
        context = {'articles': queryset}
        template_name='news/year_archive.html'

