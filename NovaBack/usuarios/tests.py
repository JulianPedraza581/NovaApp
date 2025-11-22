from django.test import TestCase
from .models import Usuario

# Create your tests here.
class UsuarioModelTest(TestCase):

    def test_creacion_usuario(self):
        # Crear usuario
        usuario = Usuario.objects.create_user(
            username="juan123",
            password="password_seguro",
            email="juan@example.com",
            telefono="555123456",
            presupuesto_mensual=1500.50,
        )

        # Verificaciones
        self.assertIsNotNone(usuario.id)
        self.assertEqual(usuario.username, "juan123")
        self.assertEqual(usuario.email, "juan@example.com")
        self.assertEqual(usuario.telefono, "555123456")
        self.assertEqual(usuario.presupuesto_mensual, 1500.50)

        # Verificar que la contraseña se guarda hasheada
        self.assertTrue(usuario.check_password("password_seguro"))

        # Verificar fechas automáticas
        self.assertIsNotNone(usuario.created_at)
        self.assertIsNotNone(usuario.updated_at)

        
    """def balance_test(self):
        user = Usuario.objects.create(username='balanceuser', password='balancepass', balance=100)
        self.assertEqual(user.balance, 100)
        
    def positive_balance_test(self):
        user = Usuario.objects.create(username='positiveuser', password='positivepass', balance=50)
        self.assertGreaterEqual(user.balance, 0)
        """