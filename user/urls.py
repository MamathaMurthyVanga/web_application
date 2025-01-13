from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('app/<int:id>', views.app, name='app'),
    path('points', views.points, name='points'),
    path('task', views.task, name='task'),


   
]