from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate
from usuarios.models import Usuario
from .serializers import (
    UsuarioSerializer, 
    UsuarioCreateSerializer, 
    UsuarioConMetasSerializer, 
    UsuarioConTransaccionesSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCreateSerializer
        elif self.action == 'metas':
            return UsuarioConMetasSerializer
        elif self.action == 'transacciones':
            return UsuarioConTransaccionesSerializer
        return UsuarioSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=self.request.user.id)
    
    def get_object(self):
        if self.kwargs.get('pk') == 'me':
            return self.request.user
        return super().get_object()
    
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def metas(self, request, pk=None):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def transacciones(self, request, pk=None):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario)
        return Response(serializer.data)