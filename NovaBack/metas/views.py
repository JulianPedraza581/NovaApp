from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Meta, AporteMeta
from .serializers import MetaSerializer, MetaCreateSerializer, AporteMetaSerializer, AporteMetaCreateSerializer

class MetaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return MetaCreateSerializer
        return MetaSerializer
    
    def get_queryset(self):
        return Meta.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class AporteMetaViewSet(viewsets.ModelViewSet):
    serializer_class = AporteMetaSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return AporteMeta.objects.filter(meta__usuario=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AporteMetaCreateSerializer
        return AporteMetaSerializer
    
    def perform_create(self, serializer):
        meta_id = self.request.data.get('meta')
        try:
            meta = Meta.objects.get(id=meta_id, usuario=self.request.user)
            serializer.save(meta=meta)
        except Meta.DoesNotExist:
            from rest_framework import serializers
            raise serializers.ValidationError("Meta no encontrada o no pertenece al usuario")