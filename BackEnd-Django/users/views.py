from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect

from .serializers import UserSerializer
# Create your views here.

@api_view(['POST'])
def register_user(request):
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@csrf_protect
@api_view(['POST'])
def login_user(request):
    username=request.data.get('username')
    password=request.data.get('password')

    user=authenticate(
        request,
        username=username,
        password=password)

    if user is None:
        return Response(
            {'error':'Invalid username or password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    login(request,user)
    return Response(
        {'message':'Login successful'},
        status=status.HTTP_200_OK
    )

@ensure_csrf_cookie
@api_view(['GET'])
def csrf_token(request):
    return Response({'csrfToken': get_token(request)})