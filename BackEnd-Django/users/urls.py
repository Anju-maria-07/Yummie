from django.urls import path
from . import views

urlpatters= [
    path('register/', views.register_user, name='register'),
]