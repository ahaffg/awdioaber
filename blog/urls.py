from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]
