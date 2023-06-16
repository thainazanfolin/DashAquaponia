from rest_framework import serializers

from .models import DashModel, User

class DashSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashModel
        # fields = ('qtdeAlimentoPeixe', 'limpezaAgua', 'peixeMorto', 'capacidadeTanque', 'nomeCliente', 'statusTanque', 'valorAlface', 'valorPeixe', 'dataInspecao', 'idCliente', 'idTanque', 'qtdeAgua', 'qtdeAlfaceColhida', 'qtdeAlfacePlantada', 'qtdePeixesTanque')
        fields = '__all__'
