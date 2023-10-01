from django.urls import path
from GameApp import views as views

urlpatterns = [
    path('', views.home),
    path('Game/',views.game,name='startGame')
]
