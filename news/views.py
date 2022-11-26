from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CommentForm, PunchIn
from .models import Article, Reporter, Comment
from django.views import generic


# Create your views here.
@login_required
def index(request):
    num_vendor = Reporter.objects.count()
    num_visit = request.session.get('num_visit', 0)
    request.session['num_visit'] = num_visit + 1
    context = {'num_vendor': num_vendor, 'num_visit': num_visit}
    return render(request, 'news/index.html', context)


class ArticleListViewForExternal(LoginRequiredMixin, generic.ListView):
    model = Article
    template_name = 'news/article_list.html'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Article List'
        return context

    def get_queryset(self):
        return Article.objects.all()


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = Article.objects.get(id=self.kwargs.get('id'))
        return obj

    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = Comment.objects.filter(article_id=self.kwargs.get('id'))
        kwargs['form'] = CommentForm
        return super().get_context_data(**kwargs)


class CommentFormView(generic.FormView):
    form_class = CommentForm
    template_name = 'news/article_detail.html'

    def form_valid(self, form):
        tar_article = get_object_or_404(Article, pk=self.kwargs['id'])
        comments = form.save(commit=False)
        comments.article = tar_article
        comments.user = self.request.user
        comments.save()
        self.success_url = tar_article.get_absolute_url()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        print(self.kwargs)
        tar_article = get_object_or_404(Article, pk=self.kwargs['id'])
        return render(self.request, 'news/article_detail.html', context={
            'form': form,
            'article': tar_article,
            'comment_list': tar_article.comment_set.all()
        })


def get_mood(request):
    if request.method == 'POST':
        forms = PunchIn(request.POST)
        if forms.is_valid():
            return HttpResponseRedirect('/')
    else:
        forms = PunchIn()
    return render(request, 'news/punch_in.html', {'forms': forms})

# @login_required
# def post_comment(request, article_id):
#     article = get_object_or_404(Article, id=article_id)
#     if request.method == 'POST':
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             new_comment = comment.save(commit=False)
#             new_comment.article = article
#             new_comment.user = request.user
#             new_comment.save()
#             return redirect(article)
#         else:
#             return HttpResponse("Please check input.")
#     else:
#         return HttpResponse("post method required.")
