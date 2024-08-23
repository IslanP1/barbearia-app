from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Horario, Agendamento
from django.http import HttpResponse

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
        
        messages.success(request, "Agendamento realizado com sucesso.")
        return redirect('/')
        
    else:
        horarios = Horario.objects.all()
        return render(request, 'agendamento.html', {'horarios': horarios})
