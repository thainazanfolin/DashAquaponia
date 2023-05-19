from django.urls import path, include
from . import views

app_name = 'DashAquaponia'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('login/', views.loginFormView, name="registerForm")
]