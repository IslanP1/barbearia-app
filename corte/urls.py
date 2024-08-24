from django.urls import path
from . import views

urlpatterns = [
    path('agendar/', views.agendar, name="agendar"),
    path('deletar/<int:id>', views.deletar, name="deletar"),
]