from rest_framework import serializers
from .models import Meta, AporteMeta

class MetaSerializer(serializers.ModelSerializer):
    progreso = serializers.ReadOnlyField()
    falta_ahorrar = serializers.ReadOnlyField()
    mayor_ahorro = serializers.ReadOnlyField()
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Meta
        fields = [
            'id',
            'usuario',
            'usuario_username',
            'nombre',
            'meta_monto',
            'ahorro_actual', 
            'tiempo_estimado',
            'fecha_objetivo',
            'color',
            'imagen',
            'progreso',
            'falta_ahorrar',
            'mayor_ahorro',
            'created_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 'progreso', 'falta_ahorrar', 'mayor_ahorro', 
            'created_at', 'updated_at'
        ]
    
    def validate_meta_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto meta debe ser mayor a cero")
        return value
    
    def validate_ahorro_actual(self, value):
        if value < 0:
            raise serializers.ValidationError("El ahorro actual no puede ser negativo")
        return value

class MetaCreateSerializer(serializers.ModelSerializer):
    """Serializer específico para creación sin campos calculados"""
    class Meta:
        model = Meta
        fields = [
            'usuario',
            'nombre',
            'meta_monto', 
            'ahorro_actual',
            'tiempo_estimado',
            'fecha_objetivo',
            'color',
            'imagen'
        ]
class AporteMetaSerializer(serializers.ModelSerializer):
    meta_nombre = serializers.CharField(source='meta.nombre', read_only=True)
    
    class Meta:
        model = AporteMeta
        fields = [
            'id',
            'meta',
            'meta_nombre',
            'monto',
            'fecha',
            'notas'
        ]
        read_only_fields = ['id', 'fecha']
    
    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a cero")
        return value

class AporteMetaCreateSerializer(serializers.ModelSerializer):
    """Serializer específico para creación de aportes"""
    class Meta:
        model = AporteMeta
        fields = ['meta', 'monto', 'notas']