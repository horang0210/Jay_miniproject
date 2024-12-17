from django.urls import path, include
from rest_framework import urls
from .views import RegisterView, UserDetailView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('api/', include('rest_framework.urls')),
    path('userdetail/', UserDetailView.as_view(), name='userdetail'),
    path('api-auth/logout/', LogoutView.as_view(), name='logout'),

] 
