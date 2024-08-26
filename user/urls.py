from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name="cadastrar"),
    path('logar/', views.logar, name="logar"),
    path('sair', views.sair, name="sair")
]