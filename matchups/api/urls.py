# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.player_analysis, name='player_analysis'),
]
