from django.shortcuts import render
from .models import Article, Reporter
from django.views import generic


# Create your views here.
def index(request):
    context = {'msg': ' Hello World! '}
    return render(request, 'news/index.html', context)


class ArticleListView(generic.ListView):
    model = Article
    template_name = 'news/article_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Article List'
        return context

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'new/article_detail.html'

    def get_context_data(self, **kwargs):
        context=super(ArticleDetailView, self).get_context_data(**kwargs)
        context['article']=Article.objects.filter(id=self.pk_url_kwarg)
        return context
