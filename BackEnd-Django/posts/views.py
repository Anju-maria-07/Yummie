from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PostSerializer

# Create your views here.
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)