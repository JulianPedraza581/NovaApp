from django.forms import ValidationError
from django.test import TestCase
from .models import Transaccion
from usuarios.models import Usuario
# Create your tests here.

class TransaccionTestCase(TestCase):

    def crear_transaccion(self):

        Transaccion(
            usuario = None,
            concepto="Pago Universidad",
            monto = 1000,
            notas = "Pago de la matrícula, del semestre 7"
        )

        self.assertTrue(Transaccion.objects.exists())



    def verificar_usuario_transaccion(self):
        Transaccion(
            usuario = None,
            concepto="Pago Universidad",
            monto = 1000,
            notas = "Pago de la matrícula, del semestre 7"
        )

        self.assertEqual(Transaccion.objects.all()[0].usuario.nombre,usuario.nombre)

    
    def verificar_error_valor_negativo(self):
        Transaccion(
            usuario = None,
            concepto="Pago Universidad",
            monto = 1000,
            notas = "Pago de la matrícula, del semestre 7"
        )

        with self.assertRaises(ValidationError):
            Transaccion.objects.create(
                usuario=None,
                nombre=None,
                meta_monto=None,  
                ahorro_actual=None,
                tiempo_estimado=None,
                fecha_objetivo=None,
                imagen=None,
            )



'''
def save(self, *args, **kwargs):
        self.full_clean()  # ← activa validadores
        super().save(*args, **kwargs)

    concepto = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
'''