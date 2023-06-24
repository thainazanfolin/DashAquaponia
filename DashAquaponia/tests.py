from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import DashModel
from .views import HomeView, IndexView

import DashAquaponia.urls

class DashModelTestCase(TestCase):
    def setUp(self):
        self.dash_model = DashModel.objects.create(
            qtdeAlimentoPeixe=100,
            limpezaAgua="Sim",
            peixeMorto="Não",
            capacidadeTanque=1000,
            nomeCliente="Teste",
            statusTanque="Ativo",
            valorAlface=2.5,
            valorPeixe=5.0,
            dataInspecao="2023-06-24",
            idCliente=1,
            idTanque=1,
            qtdeAgua=200,
            qtdeAlfaceColhida=50,
            qtdeAlfacePlantada=100,
            qtdeAlfaceTotal=150,
            qtdePeixesTanque=20
        )

    def test_dash_model_creation(self):
        self.assertEqual(self.dash_model.qtdeAlimentoPeixe, 100)
        self.assertEqual(self.dash_model.limpezaAgua, "Sim")
        self.assertEqual(self.dash_model.peixeMorto, "Não")
        self.assertEqual(self.dash_model.capacidadeTanque, 1000)
        self.assertEqual(self.dash_model.nomeCliente, "Teste")
        self.assertEqual(self.dash_model.statusTanque, "Ativo")
        self.assertEqual(self.dash_model.valorAlface, 2.5)
        self.assertEqual(self.dash_model.valorPeixe, 5.0)
        self.assertEqual(self.dash_model.dataInspecao, "2023-06-24")
        self.assertEqual(self.dash_model.idCliente, 1)
        self.assertEqual(self.dash_model.idTanque, 1)
        self.assertEqual(self.dash_model.qtdeAgua, 200)
        self.assertEqual(self.dash_model.qtdeAlfaceColhida, 50)
        self.assertEqual(self.dash_model.qtdeAlfacePlantada, 100)
        self.assertEqual(self.dash_model.qtdeAlfaceTotal, 150)
        self.assertEqual(self.dash_model.qtdePeixesTanque, 20)
        

class IndexViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

class LoginTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            email="teste@email.com",
            password="12345",
            first_name="Usuario",
            last_name="Teste"
        )

    def test_perfil_view_authenticated(self):
        self.client.login(email="teste@email.com", password="12345")
        response = self.client.get('/perfil/')
        self.assertEqual(response.status_code, 200)

    def test_home_view_unauthenticated(self):
        response = self.client.get('/home')
        self.assertRedirects(response, '/login/?next=/home')
