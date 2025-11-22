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

# Create your views here.
class UsuarioAPIView(APIView):

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UsuarioCreateAPIView(APIView):

    def get(self, request):
        usuarios = Usuario.objects.all()   # ✔ Aquí va el MODELO
        serializer = UsuarioCreateSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
