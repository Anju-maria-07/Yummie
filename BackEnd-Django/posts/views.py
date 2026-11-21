from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .pagination import PostPagination
from rest_framework.response import Response
from rest_framework import status

from .serializers import PostSerializer
from .models import Post, PostLike
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

class LikePostView(generics.GenericAPIView):
    queryset=Post.objects.all()
    permission_classes=[IsAuthenticated]

    def post(self,request,*args,**kwargs):
        post=self.get_object()
        like , created =PostLike.objects.get_or_create(
            post=post,
            user=request.user
        )

        if created:
            return Response(
                {'message':'Post Liked Successfully'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {'message':'Already liked the post'},
            status=status.HTTP_200_OK
        )

class UnlikePostView(generics.GenericAPIView):
    queryset=Post.objects.all()
    permission_classes=[IsAuthenticated]

    def delete(self,request,*args,**kwargs):
        post=self.get_object()

        like=PostLike.objects.filter(
            post=post,
            user=request.user
        ).first()

        if like is None:
            return Response(
            {'message':'you have not liked the post yet.'},
            status=status.HTTP_404_NOT_FOUND
            )

        like.delete()
        return Response(
            {'message':'unliked the post successfully'},
            status=status.HTTP_200_OK
        )
           