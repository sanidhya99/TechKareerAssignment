# TODO There's certainly more than one way to do this task, so take your pick.


from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer

# Define the pagination class
class PostPagination(PageNumberPagination):
    page_size = 10  # Adjust as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create a generic ListAPIView for posts
class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by('-timestamp')
    serializer_class = PostSerializer
    pagination_class = PostPagination
