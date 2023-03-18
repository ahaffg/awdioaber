from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_replays, name='replays'),
    path('<int:replay_id>/', views.replay_detail, name='replay_detail'),
    path('add/', views.add_replay, name='add_replay'),
    path('edit/<int:replay_id>/', views.edit_replay, name='edit_replay'),
    path('delete/<int:replay_id>/', views.delete_replay, name='delete_replay')
]
