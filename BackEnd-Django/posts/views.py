from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import PostSerializer

# Create your views here.
class CreatePostView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

    def post(self,request,*args,**kwargs):
        print(request.FILES)
        print(request.FILES.getlist('media_files'))

        return super().post(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)