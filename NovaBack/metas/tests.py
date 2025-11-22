from django.forms import ValidationError
from django.test import TestCase
from .models import Meta, AporteMeta
from usuarios.models import Usuario
# Create your tests here.


class MetaTestCase(TestCase):

    def test_crear_meta(self):
        # Usuario
        username = "Joel"
        password = "1234"
        phone = '3059827384'
        budget = 100000

        # Meta
        name = 'Licuadora'
        ammount = 10000
        actual_ammount = 1000
        estimated_time = '1 año'
        aim_date = '2025-02-15'
        image = 'imagen.com'

        user = Usuario.objects.create(
            username = username,
            password = password,
            telefono = phone,
            presupuesto_mensual = budget
        )

        Meta.objects.create(
            usuario = user,
            nombre = name,
            meta_monto = ammount,
            ahorro_actual = actual_ammount,
            tiempo_estimado = estimated_time,
            fecha_objetivo = aim_date,
            imagen = image
        )

        correct_name = Meta.objects.all()[0].nombre

        self.assertEqual(correct_name, name)


    def test_longitud_metas(self):
        username = "Dayana"
        password = 'Gat0s'
        phone = '3654427384'
        budget = 100000

        name1 = 'Comprar Moto'
        ammount1 = 10000
        actual_ammount1 = 10000
        estimated_time1 = '1 año'
        aim_date1 = '2026-12-15'
        image1 = 'image.com'

        name2 = 'Viaje a Paris'
        ammount2 = 12000
        actual_ammount2 = 1300
        estimated_time2 = '3 años'
        aim_date2 = '2026-03-20'
        image2 = 'image.com'

        user = Usuario.objects.create(
            username = username,
            password = password,
            telefono = phone,
            presupuesto_mensual = budget
        )

        Meta.objects.create(
            usuario = user,
            nombre = name1,
            meta_monto = ammount1,
            ahorro_actual = actual_ammount1,
            tiempo_estimado = estimated_time1,
            fecha_objetivo = aim_date1,
            imagen = image1
        )

        Meta.objects.create(
            usuario = user,
            nombre = name2,
            meta_monto = ammount2,
            ahorro_actual = actual_ammount2,
            tiempo_estimado = estimated_time2,
            fecha_objetivo = aim_date2,
            imagen = image2
        )

        size_metas = len(Meta.objects.all())

        self.assertEqual(size_metas,2)

    def test_monto_invalido(self):
        # Usuario
        username = 'Victor'
        password = 'MiViajeFavorito'
        phone = '3514027384'
        budget = 140000

        # Meta
        name = 'Comprar Carro'
        ammount = 20000
        actual_ammount = -5000
        estimated_time = '13 meses'
        aim_date = '2026-10-2'
        image = 'imagen.com'

        user = Usuario.objects.create(
            username = username,
            password = password,
            telefono = phone,
            presupuesto_mensual = budget
        )

        with self.assertRaises(ValidationError):
            Meta.objects.create(
                usuario=user,
                nombre=name,
                meta_monto=ammount,  
                ahorro_actual=actual_ammount,
                tiempo_estimado=estimated_time,
                fecha_objetivo=aim_date,
                imagen=image,
            )



