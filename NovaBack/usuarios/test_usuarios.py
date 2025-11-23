from django.test import TestCase
from .models import Usuario

class UsuarioModelTest(TestCase):

    def test_creacion_usuario(self):
        # ARRANGE
        datos_usuario = {
            "username": "juan123",
            "password": "password_seguro",
            "email": "juan@example.com",
            "telefono": "555123456",
            "presupuesto_mensual": 1500.50,
        }

        # ACT
        usuario = Usuario.objects.create_user(**datos_usuario)

        # ASSERT
        self.assertIsNotNone(usuario.id)
        self.assertEqual(usuario.username, datos_usuario["username"])
        self.assertEqual(usuario.email, datos_usuario["email"])
        self.assertEqual(usuario.telefono, datos_usuario["telefono"])
        self.assertEqual(usuario.presupuesto_mensual, datos_usuario["presupuesto_mensual"])
        self.assertTrue(usuario.check_password(datos_usuario["password"]))
        self.assertIsNotNone(usuario.created_at)
        self.assertIsNotNone(usuario.updated_at)


    def test_presupuesto_asignado_correctamente(self):
        # ARRANGE
        presupuesto = 200

        # ACT
        usuario = Usuario.objects.create_user(
            username="user1",
            password="pass",
            presupuesto_mensual=presupuesto
        )

        # ASSERT
        self.assertEqual(usuario.presupuesto_mensual, presupuesto)


    def test_presupuesto_es_positivo(self):
        # ARRANGE
        presupuesto = 500

        # ACT
        usuario = Usuario.objects.create_user(
            username="user2",
            password="pass",
            presupuesto_mensual=presupuesto
        )

        # ASSERT
        self.assertGreaterEqual(usuario.presupuesto_mensual, 0)
