from rest_framework import serializers

from .models import DashModel

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DashModel
        fields = ('qtdeAlimentoPeixe', 'limpezaAgua', 'peixeMorto', 'capacidadeTanque', 'nomeCliente', 'statusTanque', 'valorAlface', 'valorPeixe', 'dataInspecao', 'idCliente', 'idTanque', 'qtdeAgua', 'qtdeAlfaceColhida', 'qtdeAlfacePlantada', 'qtdePeixesTanque')