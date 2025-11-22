from django.test import TestCase
from .models import Meta, AporteMeta
# Create your tests here.


class MetaTestCase(TestCase):

    def test_crear_meta(self):
        Meta.objects.create(
            usuario = 1,
            nombre = 'Licuadora',
            meta_monto = 10000,
            ahorro_actual = 1000,
            tiempo_estimado = '1 año',
            fecha_objetivo = '2025-02-15',
            imagen = 'imagen.com',
            completada = True,
        )

        self.assertEqual(Meta.objects.all()[0].nombre, 'Licuadora')


    def test_longitud_metas(self):

        Meta.objects.create(
            usuario = 1,
            nombre = 'Compar Moto',
            meta_monto = 10000,
            ahorro_actual = 10000,
            tiempo_estimado = '1 año',
            fecha_objetivo = '2025-02-15',
            imagen = 'imagen.com',
        )

        Meta.objects.create(
            usuario = 2,
            nombre = 'Luisa',
            meta_monto = 12000,
            ahorro_actual = 1300,
            tiempo_estimado = '3 año',
            fecha_objetivo = '2025-02-30',
            imagen = 'imagen.com',
        )

        self.assertEqual(len(Meta.objects.all()),2)




