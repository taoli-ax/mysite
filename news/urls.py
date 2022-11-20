from django.urls import path

from .views import index,year_archive

urlpatterns = [
    path('', index, name='index'),
    path('international/', year_archive, name='international'),
]
