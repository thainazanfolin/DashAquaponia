from django.db import models as django_models, models

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
