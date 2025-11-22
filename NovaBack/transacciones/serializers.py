from rest_framework import serializers
from .models import Transaccion

class TransaccionSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Transaccion
        fields = [
            'id',
            'usuario',
            'usuario_username', 
            'concepto',
            'monto',
            'fecha',
            'notas',
            'created_at'
        ]
        read_only_fields = ['id', 'fecha', 'created_at']
    
    def validate_monto(self, value):
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor a cero")
        return value

class TransaccionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaccion
        fields = ['usuario', 'concepto', 'monto', 'notas']

# Serializador básico para usar en otros apps
class TransaccionBasicaSerializer(serializers.ModelSerializer):
    """Para usar en otros serializadores"""
    class Meta:
        model = Transaccion
        fields = ['id', 'concepto', 'monto', 'fecha']