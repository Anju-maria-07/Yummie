from django.urls import path
from . import views 

urlpatterns=[
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('', views.PostListView.as_view(), name='post-list')
]