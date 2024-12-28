from django.urls import path
from apps.demo.views import PostListAPIView

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
]
