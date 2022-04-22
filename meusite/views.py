from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from banco.models import Bank
from lista.forms import PostForm
from lista.models import ListaUser


def index(request):
    bank = Bank.objects.all()
    return render(request, 'meusite/index.html', {'bank':bank})

def anime(request, pk):
    animes = get_object_or_404(Bank, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.anime = Bank.objects.get(pk=pk)
            task.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'meusite/animes.html', {'animes' : animes, 'form': form})

def catalogo(request):
    bank = Bank.objects.all()
    return render(request, 'meusite/catalogo.html', {'bank':bank})

def contatos(request):
    dice = {}
    if request.method == 'POST':
        dice['nome'] = request.POST.get('nome')
        dice['email'] = request.POST.get('email')
        dice['mensagem'] = request.POST.get('mensagem')

        send_mail(
            dice['nome'],
            'Remetente: ' + dice['email'] + '\n\n' + dice['mensagem'],
            '',
            # [settings.EMAIL_HOST_USER],
            [settings.EMAIL_BACKEND],
        )
        return redirect('/')
    return render(request, 'meusite/contatos.html', dice)

def sobre(request):
    return render(request, 'meusite/sobre.html')

@login_required
def profile(request, pk):
    animess = ListaUser.objects.filter(user_id=pk)
    animes = Bank.objects.filter(id__in={instance.anime_id for instance in animess})
    return render(request, 'meusite/user.html', {'animes' : animes})


def view_404(request, exception):
    bank = Bank.objects.all()
    return render(request, 'meusite/index.html', {'bank':bank})