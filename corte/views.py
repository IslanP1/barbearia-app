from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Horario, Agendamento
from django.db.models import IntegerField, Value
from django.db.models.functions import Cast, Substr, Length, Concat, Replace


def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

def agendar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            horario_id = request.POST.get('horario')
            data = request.POST.get('data')
            modelo_corte = request.POST.get('modelo_corte')
            
            #Verifica se já existe um agendamento para o mesmo horário e data
            if Agendamento.objects.filter(horario_id=horario_id, data=data).exists():
                messages.error(request, 'Tem agenda marcada nessa hora e dia')
                return redirect('/agendar/')
            
            #Cria o novo agendamento se não houver conflito
            try:
                agendamento = Agendamento(
                    user=request.user,
                    horario_id=horario_id,
                    data=data,
                    modelo_corte=modelo_corte
                )
                messages.success(request, 'Agendamento realizado com sucesso')
                agendamento.save()
            except:
                messages.error(request, 'Preencha o formulário')
                return redirect('/agendar/')
        
            return redirect('/agendar/')
        
        else:
            horarios = Horario.objects.annotate(
                hora_inicial = Cast(Substr('horario', 1, 2), IntegerField())
            ).order_by('hora_inicial')
            
            agendamentos_ocupados = Agendamento.objects.annotate(
                hora_inicial=Cast(Substr('horario__horario', 1, 2), IntegerField())
            ).order_by('data', 'hora_inicial')
            
            agendamentos = Agendamento.objects.filter(user=request.user)
            
            agendamentos = agendamentos.annotate(
                hora_inicial=Cast(Substr('horario__horario', 1, 2), IntegerField())
            ).order_by('data', 'hora_inicial')
            
            return render(request, 'agendamento.html', {'horarios': horarios, 'agendamentos': agendamentos, 'agendamentos_ocupados' : agendamentos_ocupados})
        
    else:
        messages.warning(request, 'Faça autenticação para agendar ou ver agendamentos!')
        return redirect('/')
        

@login_required
def deletar(request, id):
    try:
        agendamento = Agendamento.objects.filter(user=request.user).get(id=id)
    except Agendamento.DoesNotExist:
        messages.error(request, 'Tentando apagar corte dos outro espertinho')
        return redirect('/')
    if request.method == 'POST':
        agendamento.delete()
        messages.success(request, 'Agendamento cancelado com sucesso')
        return redirect('/agendar/')
    
def agendageral(request):
    if request.method == "GET":
        if request.user.is_authenticated and request.user.is_staff:
            agendamentos = Agendamento.objects.all()
            
            agendamentos = agendamentos.annotate(
                hora_inicial=Cast(Substr('horario__horario', 1, 2), IntegerField())
            ).order_by('data', 'hora_inicial')
            
            return render(request, 'agendageral.html', {"agendamentos": agendamentos})
        messages.error(request, 'Entre como administrador')
        return redirect('/')
