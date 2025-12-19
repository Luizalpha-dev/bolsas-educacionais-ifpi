from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nova/', views.criar_bolsa, name='criar_bolsa'),
    path('editar/<int:id>/', views.editar_bolsa, name='editar_bolsa'),
    path('excluir/<int:id>/', views.excluir_bolsa, name='excluir_bolsa'),
]
