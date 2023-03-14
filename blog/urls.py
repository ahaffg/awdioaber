from django.urls import path
from blog.views import (
    BlogListView,
    SearchView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogAuthorPageView,
    like,
    CategoryView


)

app_name = 'blog'

urlpatterns = [

    path('', BlogListView.as_view(), name='list'),
    path('search/', SearchView.as_view(), name='search'),
    path('create/',  BlogCreateView.as_view(), name='create'),
    path('<slug>/', BlogDetailView.as_view(), name='details'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete/',  BlogDeleteView.as_view(), name='delete'),
    path('category/<str:category>/', CategoryView, name='category'),
    path('author/<int:pk>/',
         BlogAuthorPageView.as_view(), name='author'),
    path('like/<slug>/', like, name='like')
]
