from rest_framework import viewsets, permissions
from usuarios.models import Usuario
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UsuarioSerializer, UsuarioCreateSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCreateSerializer
        return UsuarioSerializer
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Usuario.objects.all()
        return Usuario.objects.filter(id=self.request.user.id)
    
class UsuarioAPIView(APIView):

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UsuarioCreateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        usuarios = Usuario.objects.all()   # ✔ Aquí va el MODELO
        usuarios = Usuario.objects.all()   
        serializer = UsuarioCreateSerializer(usuarios, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)