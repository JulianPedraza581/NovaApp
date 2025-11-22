from rest_framework.routers import DefaultRouter
from .views import UsuarioAPIView, UsuarioCreateAPIView
from django.urls import path, include

urlpatterns = [
    path("usuarios/", UsuarioAPIView.as_view()),
    path("usuarios/crear", UsuarioCreateAPIView.as_view()),
]