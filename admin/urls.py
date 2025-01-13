from django.urls import path
from . import views  # Ensure this import is correct and views.py exists in the same directory

urlpatterns = [
    path('', views.signin, name='signin'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('admin', views.admin, name='admin'),
    path('data', views.dataget, name='dataget'),
    path('delete/<int:id>/',views.deletedata)
]
