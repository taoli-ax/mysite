from django.urls import path, include

from .views import (
    index,
    ArticleListViewForExternal,
    ArticleDetailView,
    CommentFormView,
    get_mood,
)

urlpatterns = [
    path('', index, name='index'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('externalarticlelist/', ArticleListViewForExternal.as_view(), name='articlelist'),
    path('articledetail/<int:id>',ArticleDetailView.as_view(),name='articledetail'),
    path('article/<int:id>/comment',CommentFormView.as_view(),name='comment'),
    path('punch',get_mood,name='punch')
]
