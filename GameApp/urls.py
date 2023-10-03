from django.urls import path
from GameApp import views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('Game/', views.game, name='startGame'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutaccount, name='logout'),
    path('login/',views.loginaccount,name='login'),
    path('addscore/',views.addscore,name='score'),
    path('Pscores/',views.PreviousScore,name='scores')
]
