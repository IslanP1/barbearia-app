from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('agendar/', views.agendar, name="agendar"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
]