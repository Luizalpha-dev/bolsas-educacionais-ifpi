from django.shortcuts import render, redirect, get_object_or_404
from .models import Bolsa
from .forms import BolsaForm
from django.http import HttpResponse

def home(request):
    bolsas = Bolsa.objects.all()
    return render(request, 'core/home.html', {'bolsas': bolsas})


#CRIAR BOLSA
def criar_bolsa(request):
    if request.method == 'POST':
        form = BolsaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BolsaForm()

    return render(request, 'core/form.html', {'form': form})

#EDITAR BOLSA
def editar_bolsa(request, id):
    bolsa = get_object_or_404(Bolsa, id=id)

    if request.method == 'POST':
        form = BolsaForm(request.POST, instance=bolsa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BolsaForm(instance=bolsa)

    return render(request, 'core/form.html', {'form': form})

#EXCLUIR BOLSA
def excluir_bolsa(request, id):
    bolsa = get_object_or_404(Bolsa, id=id)
    bolsa.delete()
    return redirect('home')
