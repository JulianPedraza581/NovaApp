from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet
from metas.views import MetaViewSet, AporteMetaViewSet
from transacciones.views import TransaccionViewSet
from notificaciones.views import NotificacionViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'metas', MetaViewSet, basename='meta')
router.register(r'aportes', AporteMetaViewSet, basename='aporte')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')
router.register(r'notificaciones', NotificacionViewSet, basename='notificacion')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]