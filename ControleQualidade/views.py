from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import LoteAco, EnsaioMecanico, CaracteristicaQuantitativa, CaracteristicaQualitativa  # Importe dos modelos correspondentes
from .forms import LoteAcoForm, EnsaioMecanicoForm  # Importe dos formulários correspondentes
from django.contrib import messages
from django.core.exceptions import ValidationError


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Mensagem de erro
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})
    return render(request, 'login.html')

def custom_logout_view(request):
    logout(request)
    return redirect('login.html')

def home(request):
    """
    View para a página inicial.
    """
    return render(request, 'home.html')

def avaliar_lote_view(request, numero_lote):
    lote = get_object_or_404(LoteAco, numero_lote=numero_lote)

    try:
        resultado = lote.avaliar_lote()
        if resultado == 'Pendente':
            messages.warning(request, "Lote pendente de mais ensaios.")
        elif resultado == 'Fora de Faixa':
            messages.error(request, "Lote fora da faixa de aceitação.")
        else:
            messages.success(request, "Lote dentro da faixa de aceitação.")
    except ValidationError as e:
        messages.error(request, str(e))
        return render(request, 'detalhes_lotes.html', {'lote': lote, 'erros': str(e)})

    return render(request, 'detalhes_lotes.html', {'lote': lote, 'resultado': resultado})

def criar_lote(request):
    if request.method == 'POST':
        form = LoteAcoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_lotes')
    else:
        form = LoteAcoForm()
    return render(request, 'criar_lote.html', {'form': form})

def editar_lote(request, id):
    lote = get_object_or_404(LoteAco, pk=id)
    if request.method == 'POST':
        form = LoteAcoForm(request.POST, instance=lote)
        if form.is_valid():
            form.save()
            return redirect('lista_lotes')
    else:
        form = LoteAcoForm(instance=lote)
    return render(request, 'editar_lote.html', {'form': form})

def deletar_lote(request, id):
    lote = get_object_or_404(LoteAco, pk=id)
    if request.method == 'POST':
        lote.delete()
        return redirect('lista_lotes')
    return render(request, 'deletar_lote.html', {'lote': lote})

# Listar todos os lotes
def lista_lotes(request):
    lotes = LoteAco.objects.all()
    return render(request, 'lista_lote.html', {'lotes': lotes})

def criar_ensaio(request):
    if request.method == 'POST':
        form = EnsaioMecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_lotes')
    else:
        form = EnsaioMecanicoForm()
    return render(request, 'criar_ensaio.html', {'form': form})

def editar_ensaio(request, id):
    ensaio = get_object_or_404(EnsaioMecanico, pk=id)
    if request.method == 'POST':
        form = EnsaioMecanicoForm(request.POST, instance=ensaio)
        if form.is_valid():
            form.save()
            return redirect('alguma-url-de-sucesso')
    else:
        form = EnsaioMecanicoForm(instance=ensaio)
    return render(request, 'editar_ensaio.html', {'form': form})

def deletar_ensaio(request, id):
    ensaio = get_object_or_404(EnsaioMecanico, pk=id)
    if request.method == 'POST':
        ensaio.delete()
        return redirect('lista_lotes')
    return render(request, 'deletar_ensaio.html', {'ensaio': ensaio})

def lista_caracteristicas(request):
    caracteristicas_quantitativas = CaracteristicaQuantitativa.objects.all()
    caracteristicas_qualitativas = CaracteristicaQualitativa.objects.all()
    return render(request, 'lista_caracteristicas.html', {
        'caracteristicas_quantitativas': caracteristicas_quantitativas,
        'caracteristicas_qualitativas': caracteristicas_qualitativas
    })