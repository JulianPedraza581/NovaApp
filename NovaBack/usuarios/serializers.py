from rest_framework import serializers
from usuarios.models import Usuario
from metas.models import Meta
from transacciones.models import Transaccion

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'id',
            'username',
            'email', 
            'first_name',
            'last_name',
            'telefono',
            'presupuesto_mensual',
            'is_active',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UsuarioCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'password', 
            'email',
            'first_name',
            'last_name',
            'telefono',
            'presupuesto_mensual'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        return Usuario.objects.create_user(**validated_data)

# Serializadores para relaciones anidadas
class MetaBasicaSerializer(serializers.ModelSerializer):
    """Serializer básico para metas (sin relaciones anidadas)"""
    class Meta:
        model = Meta
        fields = ['id', 'nombre', 'meta_monto', 'ahorro_actual', 'progreso']

class TransaccionBasicaSerializer(serializers.ModelSerializer):
    """Serializer básico para transacciones"""
    class Meta:
        model = Transaccion
        fields = ['id', 'concepto', 'monto', 'fecha']

class UsuarioConMetasSerializer(UsuarioSerializer):
    metas = MetaBasicaSerializer(many=True, read_only=True)
    
    class Meta(UsuarioSerializer.Meta):
        fields = UsuarioSerializer.Meta.fields + ['metas']

class UsuarioConTransaccionesSerializer(UsuarioSerializer):
    transacciones = TransaccionBasicaSerializer(many=True, read_only=True)
    
    class Meta(UsuarioSerializer.Meta):
        fields = UsuarioSerializer.Meta.fields + ['transacciones']