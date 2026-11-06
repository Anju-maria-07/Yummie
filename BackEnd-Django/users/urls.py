from django.urls import path
from . import views

urlpatterns= [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('csrf/', views.csrf_token, name='csrf_token'),
    path('me/', views.current_user, name='current_user'),
    path('logout/', views.logout_user, name='logout')
]