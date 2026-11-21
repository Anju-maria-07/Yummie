from django.urls import path
from . import views 

urlpatterns=[
    path('create/', views.CreatePostView.as_view(), name='create-post'),
    path('', views.PostListView.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/like/', views.LikePostView.as_view(), name='post-like'),
    path('<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),
]