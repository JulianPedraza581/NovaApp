from rest_framework import viewsets, permissions, filters
from rest_framework.decorators import action  # ← Agrega esta línea
from rest_framework.response import Response
from .models import Transaccion
from .serializers import TransaccionSerializer, TransaccionCreateSerializer

class TransaccionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['concepto', 'notas']
    ordering_fields = ['fecha', 'monto', 'created_at']
    ordering = ['-fecha']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TransaccionCreateSerializer
        return TransaccionSerializer
    
    def get_queryset(self):
        return Transaccion.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    
    @action(detail=False, methods=['get'])
    def resumen(self, request):
        """Resumen de transacciones del usuario"""
        transacciones = self.get_queryset()
        total = sum(t.monto for t in transacciones)
        count = transacciones.count()
        
        return Response({
            'total_transacciones': count,
            'monto_total': total,
            'ultimas_transacciones': TransaccionSerializer(
                transacciones[:5], many=True
            ).data
        })