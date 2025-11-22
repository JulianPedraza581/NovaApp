# metas/models.py
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

class Meta(models.Model):
    """Modelo para metas de ahorro"""
    
    COLORES = [
        ('#FFB4A8', 'Coral'),
        ('#FFCBA8', 'Durazno'),
        ('#E8F48C', 'Amarillo Claro'),
        ('#B8E6B8', 'Verde Claro'),
        ('#B4D4FF', 'Azul Claro'),
        ('#FFD6EC', 'Rosa Claro'),
    ]
    

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='metas'
    )
    nombre = models.CharField(max_length=100)
    meta_monto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    ahorro_actual = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(0)]
    )
    tiempo_estimado = models.CharField(
        max_length=50,
        help_text="Ej: 365 días, 12 meses"
    )
    fecha_objetivo = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7, choices=COLORES, default='#FFB4A8')
    imagen = models.CharField(max_length=1000, default='general')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'metas'
        verbose_name = 'Meta'
        verbose_name_plural = 'Metas'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.nombre} - {self.usuario.username}"

    @property
    def progreso(self):
        """Calcula el porcentaje de progreso"""
        if self.meta_monto == 0:
            return 0
        porcentaje = (self.ahorro_actual / self.meta_monto) * 100
        return min(round(porcentaje, 2), 100)

    @property
    def falta_ahorrar(self):
        """Calcula cuánto falta para completar la meta"""
        return max(self.meta_monto - self.ahorro_actual, 0)

    @property
    def mayor_ahorro(self):
        """Obtiene el mayor aporte individual a esta meta"""
        mayor = self.aportes.aggregate(models.Max('monto'))['monto__max']
        return mayor or 0

    def agregar_ahorro(self, monto):
        """Agrega un monto al ahorro actual"""
        self.ahorro_actual += monto
        if self.ahorro_actual >= self.meta_monto:
            self.completada = True
        self.save()


class AporteMeta(models.Model):
    """Modelo para registrar aportes individuales a una meta"""
    
    meta = models.ForeignKey(
        Meta,
        on_delete=models.CASCADE,
        related_name='aportes'
    )
    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'aportes_meta'
        verbose_name = 'Aporte a Meta'
        verbose_name_plural = 'Aportes a Metas'
        ordering = ['-fecha']

    def __str__(self):
        return f"${self.monto} a {self.meta.nombre}"

    def save(self, *args, **kwargs):
        """Override save para actualizar el ahorro de la meta"""
        es_nuevo = self.pk is None
        super().save(*args, **kwargs)
        
        if es_nuevo:
            self.meta.agregar_ahorro(self.monto)