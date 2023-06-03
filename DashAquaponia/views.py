from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .forms import DashForm
from .models import User, DashModel

import pandas as pd
import plotly.express as px


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    def get(self, request):
        # template_name = "index.html"
        return render(request, 'index.html')
    
def loginFormView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'errors': ['Email ou senha inválidos.']})
    return render(request, 'login.html')


def DashAlface(request):
    idUsuario = request.user.id
    if len(DashModel.objects.filter(idCliente = idUsuario)) > 0:
        print(idUsuario)
        df = pd.DataFrame(list(DashModel.objects.values(
            'dataInspecao', 
            'qtdeAlfaceColhida')
            .filter(idCliente = idUsuario)))
        
        hist_fig = px.histogram(df, x='dataInspecao', y ='qtdeAlfaceColhida')
        line_fig = px.line(df, x='dataInspecao', y ='qtdeAlfaceColhida')
        bar_fig = px.bar(df, x='dataInspecao', y ='qtdeAlfaceColhida')

        chart_hist = hist_fig.to_html()
        chart_line = line_fig.to_html()
        chart_bar = bar_fig.to_html()

        contexto = {
            'dash_hist' : chart_hist,
            'dash_line' : chart_line,
            'dash_bar' : chart_bar
        }
        return render(request, 'dash_teste.html', contexto)
    else:
        sem_info = "Sem informações no banco para este usuário"
        contexto = {
            'dash_hist' : sem_info,
            'dash_line' : sem_info,
            'dash_bar' : sem_info
        }
        return render(request, 'dash_teste.html', contexto)
    

def CadastroDash(request):

    data_atual = datetime.today()
    if request.method == 'POST':
        nomeCliente= request.user
        capacidadeTanque = 900
        idCliente = request.user.id
        idTanque = 1
        qtdeAlimentoPeixe = request.POST.get('qtdeAlimentoPeixe')
        limpezaAgua = request.POST.get('limpezaAgua')
        if int(request.POST.get('qtdePeixesTanque')) < 40:
            peixeMorto = "Sim"
        elif int(request.POST.get('qtdePeixesTanque')) >=40 :
            peixeMorto = "Não"
        statusTanque = request.POST.get('statusTanque')
        valorAlface = request.POST.get('valorAlface')
        valorPeixe = request.POST.get('valorPeixe')
        dataInspecao = request.POST.get('dataInspecao')
        qtdeAgua = request.POST.get('qtdeAgua')
        qtdeAlfaceColhida = request.POST.get('qtdeAlfaceColhida')
        qtdeAlfacePlantada = request.POST.get('qtdeAlfacePlantada')
        qtdePeixesTanque = request.POST.get('qtdePeixesTanque')

        DashModel.objects.create(
            nomeCliente = nomeCliente,
            idCliente = idCliente,
            capacidadeTanque = capacidadeTanque,
            idTanque = idTanque,
            qtdeAlimentoPeixe = qtdeAlimentoPeixe,
            limpezaAgua = limpezaAgua,
            peixeMorto = peixeMorto,
            statusTanque = statusTanque,
            valorAlface = valorAlface,
            valorPeixe = valorPeixe,
            dataInspecao = dataInspecao,
            qtdeAgua = qtdeAgua,
            qtdeAlfaceColhida = qtdeAlfaceColhida,
            qtdeAlfacePlantada = qtdeAlfacePlantada,
            qtdePeixesTanque = qtdePeixesTanque,
        )
        return redirect('/')
    
    if request.method == 'GET':
            form = DashForm()
    contexto = {
        'form' : form
    }
    return render(request, 'registro.html', contexto)
