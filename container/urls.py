from django.urls import path
from .views import ContainerView

urlpatterns = [
    path("", ContainerView.as_view(), name='container'),
] 