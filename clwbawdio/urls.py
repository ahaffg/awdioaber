from django.urls import path
from . import views

urlpatterns = [
    path('', views.clwbawdio, name='clwbawdio'),
    path('faqs/', views.faqs, name='faqs'),
    path('clwbs/', views.clwbs, name='clwbs'),
]
