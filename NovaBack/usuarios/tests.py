from django.test import TestCase
from .models import Usuario

# Create your tests here.

class UsuarioModelTest(TestCase):
    def test_crear_usuario(self):
        Usuario.objects.create(username='testuser', password='testpass')
        self.assertTrue(Usuario.objects.filter(username='testuser').exists())
        
    def balance_test(self):
        user = Usuario.objects.create(username='balanceuser', password='balancepass', balance=100)
        self.assertEqual(user.balance, 100)
        
    def positive_balance_test(self):
        user = Usuario.objects.create(username='positiveuser', password='positivepass', balance=50)
        self.assertGreaterEqual(user.balance, 0)