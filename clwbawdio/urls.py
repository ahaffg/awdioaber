from django.urls import path
from . import views

urlpatterns = [
    path('', views.clwbawdio, name='clwbawdio'),
    path('faqs/', views.faqs, name='faqs'),
    path('clwbs/', views.clwbs, name='clwbs'),
    path('add/', views.add_clwb, name='add_clwb'),
    path('edit/<int:clwb_id>/', views.edit_clwb, name='edit_clwb'),
    path('delete/<int:clwb_id>/', views.delete_clwb, name='delete_clwb'),
    path('<int:clwb_id>/', views.clwb_detail, name='clwb_detail'),
]
