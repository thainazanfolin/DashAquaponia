from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serializers import DashSerializer
from .forms import DashForm
from .models import User, DashModel
from django.db.models import Sum as Soma
from django.contrib import messages

import pandas as pd
import plotly.express as px


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    def get(self, request):
        # template_name = "index.html"

        return render(request, 'index.html')
    
def logoutView(request):
    messages.success(request,"Logout realizado!")
    logout(request)
    return redirect('/')

class DashBoardView(TemplateView):
    def get(self, request):
        return render(request,'servicos.html')


def LoginCadastroView(request):
    idUsuario = request.user.id
    if idUsuario is None :
        if 'email' in request.POST.keys():
            entrar = True
        else:
            entrar = False

        if entrar:
            if request.method == 'POST':
                Entraremail = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=Entraremail, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('/')
                elif user is None:
                    return render(request, 'login.html', {'errors': ['Email ou senha inválidos.']})
            return render(request, 'login.html')

        if 'CadastroEmail' in request.POST.keys():
            cadastrar = True
        else:
            cadastrar = False
    
        if cadastrar:
            if request.method == 'POST':
                cadastroEmail = request.POST['CadastroEmail']   
                InsertPassword = request.POST['CadastroPassword']
                confirmPassword = request.POST['ConfirmCadastroPassword']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                
                if InsertPassword != confirmPassword:
                    return render(request, 'login.html', {'errors' : ['Senhas divergentes.']})
                
                user = User.objects.filter(email=cadastroEmail).first()
                if user:
                    return render(request, 'login.html', {'errors': ['Email já cadastrado.']})
                
                User.objects.create_user(
                    email = cadastroEmail,
                    password = InsertPassword,
                    first_name = first_name,
                    last_name = last_name,
                )
            return render(request, 'login.html')
    if idUsuario:
        return redirect('/')
    return render(request, 'login.html')

def DashModificar(request):
    idUsuario = request.user.id
    if len(DashModel.objects.filter(idCliente = 1)) > 0:
        # print(idUsuario)
        df = pd.DataFrame(list(DashModel.objects.values(
            'dataInspecao', 
            'qtdeAlfaceColhida')
            .filter(idCliente = 1)))
        
        line_fig = px.line(df, x='dataInspecao', y ='qtdeAlfaceColhida',
                           labels = {
                               'dataInspecao': "Data",
                               'qtdeAlfaceColhida' : "Quantidade de Alface"
                           },
                           title = "Quantidade de Alface Colhido | Data")
        bar_fig = px.bar(df, x='dataInspecao', y ='qtdeAlfaceColhida',
                         labels = {
                               'dataInspecao': "Data",
                               'qtdeAlfaceColhida' : "Quantidade de Alface"
                           },
                           title = "Quantidade de Alface Colhido | Data")

        chart_line = line_fig.to_html()
        chart_bar = bar_fig.to_html()

        contexto = {
            'dash_line' : chart_line,
            'dash_bar' : chart_bar
        }
        return render(request, 'dash.html', contexto)
    else:
        sem_info = "Sem informações no banco para este usuário"
        contexto = {
            'dash_line' : sem_info,
            'dash_bar' : sem_info
        }
        return render(request, 'dash.html', contexto)

def DashAlfacePadrão(request):
    idUsuario = request.user.id
    if len(DashModel.objects.filter(idCliente = idUsuario)) > 0:
        df = pd.DataFrame(list(DashModel.objects.values(
            'dataInspecao', 
            'qtdeAlfaceColhida')
            .filter(idCliente = idUsuario)))
        
        line_fig = px.line(df, x='dataInspecao', y ='qtdeAlfaceColhida',
                           labels = {
                               'dataInspecao': "Data",
                               'qtdeAlfaceColhida' : "Quantidade de Alface"
                           },
                           title = "Quantidade de Alface Colhido | Data")
        bar_fig = px.bar(df, x='dataInspecao', y ='qtdeAlfaceColhida',
                         labels = {
                               'dataInspecao': "Data",
                               'qtdeAlfaceColhida' : "Quantidade de Alface"
                           },
                           title = "Quantidade de Alface Colhido | Data")

        chart_line = line_fig.to_html()
        chart_bar = bar_fig.to_html()

        contexto = {
            'dash_line' : chart_line,
            'dash_bar' : chart_bar
        }
        return render(request, 'dash.html', contexto)
    else:
        sem_info = "Sem informações no banco para este usuário"
        contexto = {
            'dash_line' : sem_info,
            'dash_bar' : sem_info
        }
        return render(request, 'dash.html', contexto)
    
def CadastroDash(request):

    data_atual = datetime.now()
    data_atual_str = data_atual.strftime("%Y-%m-%d")

    somaAlface = DashModel.objects.filter(idCliente = request.user.id).aggregate(Soma('qtdeAlfaceColhida'))
    somaAlfaceInt = 0
    for chave in somaAlface:
        somaAlfaceInt = somaAlface[chave]

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
        if somaAlfaceInt == None:
            qtdeAlfaceTotal = qtdeAlfaceColhida
        elif somaAlfaceInt != None:
            qtdeAlfaceTotal = somaAlfaceInt + int(qtdeAlfaceColhida)
        qtdePeixesTanque = request.POST.get('qtdePeixesTanque')

        #if len(DashModel.objects.filter(idCliente = request.user.id)) > 0:
        if dataInspecao == data_atual_str and len(DashModel.objects.values('dataInspecao').filter(idCliente = request.user.id)) >= 1:
                print("Data igual teste" + data_atual_str+ "  "+ dataInspecao)
                DashModel.objects.filter(idCliente = request.user.id,
                                        dataInspecao = data_atual_str).update(
                        nomeCliente = str(nomeCliente),
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
        elif dataInspecao == data_atual_str and len(DashModel.objects.values('dataInspecao').filter(idCliente = request.user.id)) == 0:
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
            qtdeAlfaceTotal = qtdeAlfaceTotal,
            qtdePeixesTanque = qtdePeixesTanque,
        )   
        else:
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
                qtdeAlfaceTotal = qtdeAlfaceTotal,
                qtdePeixesTanque = qtdePeixesTanque,
            )   
        return redirect('/')
    if request.method == 'GET':
            form = DashForm()
    contexto = {
        'form' : form
    }
    return render(request, 'registro.html', contexto)

def ContatoView(request):
    return render(request, 'contato.html')

def PerfilView(request):
    loggedUserId = request.user.id
    userInfo = User.objects.get(id = loggedUserId)

    if request.method == 'POST':
        userInfo.first_name = request.POST.get('first-name')
        userInfo.last_name = request.POST.get('last-name')
        userInfo.email = request.POST.get('email')
        userInfo.save()
        return redirect('/perfil')

    contexto = {
        'firstName': userInfo.get_short_name(),
        'lastName': userInfo.get_last_name(),
        'email': userInfo.get_email(),
    }
    return render(request, 'perfil.html', contexto)

class DashModelViewSet(viewsets.ModelViewSet):
    queryset = DashModel.objects.all()
    serializer_class = DashSerializer
