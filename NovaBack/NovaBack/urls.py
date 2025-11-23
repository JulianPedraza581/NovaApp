from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Importa los ViewSets
from usuarios.views import UsuarioViewSet
from metas.views import MetaViewSet, AporteMetaViewSet
from transacciones.views import TransaccionViewSet
from notificaciones.views import NotificacionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UsuarioViewSet, basename='usuario')
router.register(r'metas', MetaViewSet, basename='meta')
router.register(r'aportes', AporteMetaViewSet, basename='aporte')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')
router.register(r'notificaciones', NotificacionViewSet, basename='notificacion')

urlpatterns = [
    path("", include("django_prometheus.urls")),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]