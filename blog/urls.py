from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.all_posts, name='posts'),
    path('<int:post_id>/', views.post_view, name='post_view'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/',
         views.delete_post,
         name='delete_post'),
]