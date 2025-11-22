from django.forms import ValidationError
from django.test import TestCase
from .models import Transaccion
from usuarios.models import Usuario
# Create your tests here.

class TransaccionTestCase(TestCase):

    def test_crear_transaccion(self):
        datos_usuario = {
            "username": "juan123",
            "password": "password_seguro",
            "email": "juan@example.com",
            "telefono": "555123456",
            "presupuesto_mensual": 1500.50,
        }

        datos_transaccion = {
            "concepto": "Pago Universidad",
            "monto":1000,
            "notas":"Pago de la matrícula, semestre 7"
        }

        user = Usuario.objects.create_user(**datos_usuario)

        Transaccion.objects.create(
            usuario = user,
            concepto=datos_transaccion['concepto'],
            monto = datos_transaccion['monto'],
            notas =datos_transaccion['notas']
        )

        self.assertTrue(Transaccion.objects.exists())



    def test_verificar_nombre_usuario_transaccion(self):
        datos_usuario = {
            "username": "pablomillar",
            "password": "jamaica904",
            "email": "pablomi2@example.com",
            "telefono": "425396521",
            "presupuesto_mensual": 2030.10,
        }

        datos_transaccion = {
            "concepto": "Pago Casa",
            "monto":2500,
            "notas":"Cuota 92"
        }

        user = Usuario.objects.create_user(**datos_usuario)

        Transaccion.objects.create(
            usuario = user,
            concepto=datos_transaccion['concepto'],
            monto = datos_transaccion['monto'],
            notas = datos_transaccion['notas']
        )

        username = Transaccion.objects.all()[0].usuario.username

        self.assertEqual( username,user.username)

    
    def test_verificar_error_valor_negativo(self):
        datos_usuario = {
            "username": "pablomillar",
            "password": "jamaica904",
            "email": "pablomi2@example.com",
            "telefono": "425396521",
            "presupuesto_mensual": 2030.10,
        }

        user = Usuario.objects.create_user(**datos_usuario)

        datos_transaccion = {
            "concepto": "Pago Luz",
            "monto":-2500,
            "notas":"Febrero"
        }

        with self.assertRaises(ValidationError):
            Transaccion.objects.create(
                usuario = user ,
                concepto=datos_transaccion['concepto'],
                monto = datos_transaccion['monto'],
                notas = datos_transaccion['notas']
            )

