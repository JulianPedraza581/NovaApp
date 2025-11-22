from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from notificaciones.models import Notificacion
from .serializers import NotificacionSerializer, NotificacionCreateSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha']
    ordering = ['-fecha']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return NotificacionCreateSerializer
        return NotificacionSerializer
    
    @action(detail=False, methods=['get'])
    def recientes(self, request):
        """Obtener notificaciones recientes (últimas 10)"""
        notificaciones = Notificacion.objects.all().order_by('-fecha')[:10]
        serializer = self.get_serializer(notificaciones, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def marcar_leidas(self, request):
        """Marcar notificaciones como leídas (si tuvieran ese campo)"""
        # Si agregas campo 'leida' al modelo, aquí la lógica
        return Response({"message": "Funcionalidad para marcar como leídas"})