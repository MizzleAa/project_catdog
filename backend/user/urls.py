from django.urls import path, include
from django.conf.urls import url
from rest_framework_simplejwt import views as jwt_views

from . import views


urlpatterns = [
    path('create/', views.CreateUserView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('update/', views.UpdatePasswordView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('refresh/', views.RefreshTokenView.as_view())
]
