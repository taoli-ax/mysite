from django.urls import path

from .views import (
    index,
    ArticleListView,
    ArticleDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('articlelist/', ArticleListView.as_view(), name='articlelist'),
    path('articledetail/<article_id:article>',ArticleDetailView.as_view(),name='articledetail'),
]
