from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .pagination import PostPagination

from .serializers import PostSerializer
from .models import Post
from .permissions import IsPostOwner

# Create your views here.
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class PostListView(generics.ListAPIView):
    queryset= Post.objects.select_related('user','food_spot').prefetch_related('media')
    serializer_class= PostSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=PostPagination

class PostDetailView(generics.RetrieveAPIView):
    queryset=Post.objects.select_related(
        'user','food_spot'
        ).prefetch_related('media')

    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]

class PostUpdateView(generics.UpdateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated, IsPostOwner]

class PostDeleteView(generics.DestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated , IsPostOwner]