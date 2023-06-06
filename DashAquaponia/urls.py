from django.urls import path, include
from . import views

app_name = 'DashAquaponia'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.loginFormView, name="registerForm"),
    path('dash/', views.DashAlface, name="dash"),
    path('registro/', views.CadastroDash, name="registro-dash")
]