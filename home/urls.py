from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
    path('construction/', views.terms, name='construction'),
]
