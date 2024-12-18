from django.urls import path, include
from rest_framework import urls
from .views import RegisterView, UserDetailView, LogoutView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('userdetail/', UserDetailView.as_view(), name='userdetail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
] 
