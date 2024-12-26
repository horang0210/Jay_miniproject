from django.urls import path, include
from .views import RegisterView, DetailView, LogoutView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('detail/', DetailView.as_view(), name='detail'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
] 
