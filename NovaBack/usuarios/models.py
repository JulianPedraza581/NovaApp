# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    """Modelo extendido de usuario con campos personalizados"""
    
    telefono = models.CharField(max_length=15, blank=True, null=True)
    presupuesto_mensual = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0,
        help_text="Presupuesto mensual del usuario"
    )
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)