from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Article, Reporter
from django.views import generic


# Create your views here.
@login_required
def index(request):

    num_vendor = Reporter.objects.count()
    num_visit=request.session.get('num_visit',0)
    request.session['num_visit']=num_visit+1
    context = {'num_vendor': num_vendor,'num_visit':num_visit}
    return render(request, 'news/index.html', context)


class ArticleListViewForExternal(LoginRequiredMixin,generic.ListView):
    model = Article
    template_name = 'news/article_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Article List'
        return context

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(LoginRequiredMixin,generic.DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        obj=Article.objects.get(id=self.kwargs.get('id'))
        return obj
