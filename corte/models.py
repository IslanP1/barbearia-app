from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Horario(models.Model):
    horario = models.CharField(max_length=50)
    
    def __str__(self):
        return self.horario

class Agendamento(models.Model):
    #tratar
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    horario = models.ForeignKey(Horario, on_delete=models.PROTECT)
    data = models.DateField()
    modelo_corte = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"