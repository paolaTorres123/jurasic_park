from django.test import TestCase
from dinosaurios.models import Dinosaurio,Periodo,LONGUITUD_MAXIMA
from dinosaurios.forms import DinoForm,PeriodoForm


class TestFormDino(TestCase):

    def setUp(self, nombre='T-REX',altura='5',periodo='cretacio',descripcion='periodo chido'):
        self.periodo = Periodo(
            nombre= periodo,
            descripcion = descripcion
        )
        self.periodo.save()

        self.data = {
            'nombre' : nombre,
            'altura' : altura,
            'periodo' : Periodo.objects.first().id,

        }

    def test_dino_nombre_vacio(self):

        periodo = Periodo.objects.create(
            nombre= 'cretacio',
            descripcion = 'periodo chido'
        )
        form = DinoForm(
            data = {
                'nombre' : '',
                'altura' : '5',
                'periodo': periodo
            }
        )
        self.assertFalse(form.is_valid())

    def test_longuitud_excedida_false(self):
        self.data['nombre']='tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuvnunvfnjf  hfnjfjofuonfuonfcuonfvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnniutny'
        self.form = DinoForm(
            self.data
        )
        self.assertFalse(self.form.is_valid())
    
    def test_longuitud_excedida_true(self):
        self.data['nombre']='tuuunnnnnnnnnnnnnnniutny'
        self.form = DinoForm(
            self.data
        )
        self.assertTrue(self.form.is_valid())

    def test_max_length_nombre(self):
        self.data['nombre']='tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuunuvnunvfnjf  hfnjfjofuonfuonfcuonfvnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnniutny'
        self.form = DinoForm(
            self.data
        )
        self.assertEquals(self.form.errors['nombre'],[LONGUITUD_MAXIMA])

    def text_cantidad_mayor_28(self):
        self.data['altura']=63
        self.form = DinoForm(
            self.data
        )
        self.assertEquals(self.form.errors['altura'],['Error {0} la altura es mayor  28'.format(self.data['altura'])])