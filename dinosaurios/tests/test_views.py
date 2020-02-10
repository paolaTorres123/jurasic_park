from django.test import TestCase
from dinosaurios.models import Dinosaurio,Periodo
from dinosaurios.forms import DinoForm
from django.contrib.auth.models import User

class TestViews(TestCase):

    def test_lista_dinosaurios(self):
        respose=self.client.get('/periodo/dinos')
        self.assertEqual(respose.status_code, 200)

    def test_agrega_dino(self):
        User.objects.create_user(username='paola', password='12345')
        self.client.login(username='paola', password='12345')

        response = self.client.get('/periodo/agregar/dino')
        self.assertEqual(response.status_code, 200)

    def test_template_correcto_dinosaurios(self):
        User.objects.create_user(username='paola',password='12345')
        self.client.login(username='paola',password='12345')

        respose=self.client.get('/periodo/agregar/dino')
        self.assertTemplateUsed(respose,'nuevo.html')

    def test_template_correcto_lista_periodos(self):
        User.objects.create_user(username='paola',password='12345')
        self.client.login(username='paola',password='12345')

        respose=self.client.get('/periodo/')
        self.assertTemplateUsed(respose,'periodos.html')

    def test_redireccion_de_dinos(self):
        response = self.client.get('/periodo/agregar/dino')
        self.assertRedirects(response,'/admin/?next=/periodo/agregar/dino')
    
    def test_redireccion_de_periodos(self):
        response = self.client.get('/periodo/')
        self.assertRedirects(response,'/admin/?next=/periodo/')

    def test_agrega_dino_form(self):
        User.objects.create_user(username='paola',password='12345')
        self.client.login(username='paola',password='12345')
        data = {
            'nombre': 'Cretacio',
            'descripcion': 'periodo chidote'
        }
        self.client.post('/periodo/agregar', data=data)

        datat = {
            'nombre' : 'T-REX',
            'altura' : '8',
            'periodo' : Periodo.objects.first().id

        }
        self.client.post('/periodo/agregar/dino',data=datat)
        self.assertEqual(Dinosaurio.objects.all().count(),1)

    def test_eliminar_periodo_existente(self):
        Periodo.objects.create(
            nombre='Cretacio',
            descripcion='periodo chidote'
        )
        id = Periodo.objects.first().id
        self.client.get('/periodo/eliminar/'+str(id))
        self.assertEqual(Periodo.objects.all().count(),0)
        
    def test_eliminar_dinosaurio_no_existente(self):
        response = self.client.get('/periodo/eliminar/'+str(1))

        self.assertEqual(response.context['error'],'No se pudo encontrar el periodo')