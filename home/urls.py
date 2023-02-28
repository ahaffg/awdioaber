from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('policy/', views.policy, name='policy'),
    path('terms/', views.terms, name='terms'),
]
