from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.all_articles, name='articles'),
    path('<int:article_id>/', views.article_view, name='article_view'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:articlet_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/',
         views.article_post,
         name='article_post'),
]