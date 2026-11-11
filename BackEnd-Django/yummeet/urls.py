from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/accept/', views.accept_yummeet, name='accept-yummeet'),
]