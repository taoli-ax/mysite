from django.urls import path

from .views import (
    index,
    ArticleListViewForExternal,
    ArticleDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('externalarticlelist/', ArticleListViewForExternal.as_view(), name='articlelist'),
    path('articledetail/<int:id>',ArticleDetailView.as_view(),name='articledetail'),
]
