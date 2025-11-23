from rest_framework import serializers, permissions
from usuarios.models import Usuario
from rest_framework import viewsets
from metas.models import Meta
from transacciones.models import Transaccion


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    


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
        fields = ["username", "password", "email", "telefono"]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = Usuario(**validated_data)
        user.set_password(password)      # ← ENCRIPTA
        user.save()
        return user
