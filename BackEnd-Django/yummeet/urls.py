from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/accept/', views.accept_yummeet, name='accept-yummeet'),
    path('create/', views.CreateYumMeetView.as_view(), name='create-yummeet')
]