from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='blog'),
    path('<int:article_id>/', views.article, name='article'),
    path('add/', views.add_product, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]