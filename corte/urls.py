from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agendar/', views.agendar, name="agendar"),
    path('agendageral/', views.agendageral, name="agendageral"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
    path('feedback/', views.feedback, name="feedback"),
]