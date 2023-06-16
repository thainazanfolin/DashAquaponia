from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'DashAquaponia'

router = routers.DefaultRouter()
router.register(r'DashModel', views.DashModelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.LoginCadastroView, name="login"),
    path('dash/', views.DashAlfacePadrão, name="dash"),
    path('servicos/', views.DashBoardView.as_view(), name="servicos"),
    path('registro/', views.CadastroDash, name="registro"),
    path('contato/', views.ContatoView, name="contato"),
    path('perfil/', views.PerfilView, name="perfil"),
    path('logout/', views.logoutView, name="logout"),
    # path('CrescimentoAlface/', views.DashAlface, name="dash"),
    
]