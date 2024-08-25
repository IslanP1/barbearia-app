from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Horario, Agendamento
from django.http import HttpResponse

def home(request):
    if request.method == "GET":
        return render(request, 'home.html')

@login_required
def agendar(request):
    if request.method == "POST":
        horario_id = request.POST.get('horario')
        data = request.POST.get('data')
        modelo_corte = request.POST.get('modelo_corte')
        
        #Verifica se já existe um agendamento para o mesmo horário e data
        if Agendamento.objects.filter(horario_id=horario_id, data=data).exists():
            return HttpResponse("horario ocupado") 
        
        
        #Cria o novo agendamento se não houver conflito
        agendamento = Agendamento(
            user=request.user,
            horario_id=horario_id,
            data=data,
            modelo_corte=modelo_corte
        )
        agendamento.save()
    
        return redirect('/corte/agendar/')
        
    else:
        horarios = Horario.objects.all()
        agendamentos = Agendamento.objects.filter(user=request.user)
        return render(request, 'agendamento.html', {'horarios': horarios, 'agendamentos': agendamentos})

@login_required
def deletar(request, id):
    try:
        agendamento = Agendamento.objects.filter(user=request.user).get(id=id)
    except Agendamento.DoesNotExist:
        #tratar para não apagar os cortes de outros
        pass
    if request.method == 'POST':
        agendamento.delete()
        return redirect('/corte/agendar/')

