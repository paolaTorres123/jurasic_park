from django.test import TestCase
from dinosaurios.models import Dinosaurio, Periodo,LONGUITUD_MAXIMA
from django.core.exceptions import ValidationError


class PruebaHumo(TestCase):

    def setUp(self, nombre='T-REX',altura='5',periodo='cretacio',descripcion='periodo chido'):
        self.periodo = Periodo(
            nombre=periodo,
            descripcion=descripcion
        )
        self.dinosaurio = Dinosaurio(
            nombre=nombre,
            altura=altura,
            periodo=self.periodo,
        )

    def test_prueba_humo(self):
        self.assertEqual(2 + 2, 4)

    def test_agrega_dinosaurio(self):
        periodo = Periodo.objects.create(
            nombre='cretacio',
            descripcion='periodo chido'
        )
        dino = Dinosaurio.objects.create(
            nombre='T-REX',
            altura='5',
            periodo=periodo,
        )
        dino_uno = Dinosaurio.objects.first()

        self.assertEqual(dino_uno, dino)
        self.assertEqual(dino_uno.nombre, 'T-REX')
        self.assertEqual(str(dino_uno), 'T-REX')
        self.assertEqual(len(Dinosaurio.objects.all()), 1)
    
    def test_return_object_dino(self):
        self.periodo.save()
        self.dinosaurio.periodo=self.periodo
        self.dinosaurio.save()
        self.assertEquals(self.dinosaurio.nombre,self.dinosaurio.__str__())

    def test_max_length_nombre(self):
        self.dinosaurio.nombre='T-REX ndodfodgj'

        self.assertLess(len(self.dinosaurio.nombre),100)
    
    def test_longuitud_excedida_dino(self):
        self.dinosaurio.nombre='tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuvnunvfnjf  hfnjfjofuonfuonfcuonfvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnniutny'

        with self.assertRaises(ValidationError)as exception:
            self.dinosaurio.full_clean()

    def test_prueba_texto_error(self):
        self.dinosaurio.nombre='itttttttttttttttttttttttttttttggggggggggkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdooodddddddddddddddddddddddddddddddddddddpppppppppppppppp'

        try:
            self.dinosaurio.full_clean()
        except ValidationError as ex:
            msg= str(ex.message_dict['nombre'][0])
            self.assertEquals(msg,LONGUITUD_MAXIMA)

        #LAS validaciones son en formulario
        #lo que se hace en formularios

    def test_insercion_dino(self):
        self.periodo.save()
        self.dinosaurio.periodo=self.periodo
        self.dinosaurio.save()

        self.assertEquals(Dinosaurio.objects.all()[0],self.dinosaurio)

    def test_insercion_del_nomre_de_dino(self):
        self.periodo.save()
        self.dinosaurio.periodo=self.periodo
        self.dinosaurio.save()

        dinosaurio = Dinosaurio.objects.first()
        self.assertEquals(dinosaurio.nombre,'T-REX')  