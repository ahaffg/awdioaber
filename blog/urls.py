from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='blog'),
    path('article/', views.article, name='article')
]