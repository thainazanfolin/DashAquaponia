from django.db import models as django_models, models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class DashModel(django_models.Model):
    qtdeAlimentoPeixe = models.IntegerField(verbose_name='AlimentoPeixe')
    limpezaAgua = models.BooleanField(verbose_name="LimpezaAgua")
    peixeMorto = models.BooleanField(verbose_name="PeixeMorto")
    capacidadeTanque = models.FloatField(verbose_name="CapacidadeTanque")
    nomeCliente = models.CharField(verbose_name="Cliente", max_length=75)
    statusTanque = models.CharField(verbose_name="Status",  max_length=75)
    valorAlface = models.FloatField(verbose_name="ValorAlface")
    valorPeixe = models.FloatField(verbose_name="ValorPeixe")
    dataInspecao = models.DateField(verbose_name="Data")
    idCliente = models.IntegerField(verbose_name="IdCliente")
    idTanque = models.IntegerField(verbose_name="IdTanque")
    qtdeAgua = models.FloatField(verbose_name="qtdeAgua")
    qtdeAlfaceColhida =  models.IntegerField(verbose_name="AlfaceColhido")
    qtdeAlfacePlantada = models.IntegerField(verbose_name="AlfacePlantado")
    qtdePeixesTanque = models.IntegerField(verbose_name="PeixesNoTanque")

    class Meta:
        db_table = 'AquaDash'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # cria um novo usuário
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Create and save a superuser
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(email, password, **extra_fields)

class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(unique=True, max_length=10000)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email