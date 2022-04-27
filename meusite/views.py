from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from banco.models import Bank
from lista.forms import PostForm
from lista.models import ListaUser
import datetime


def index(request):
    bank = Bank.objects.all()
    print('Acesso a Home: '+request.user.username+' '+str(datetime.datetime.now()))
    return render(request, 'meusite/index.html', {'bank':bank})

def anime(request, pk):
    print('Acesso a Página de Anime: '+request.user.username+' '+str(datetime.datetime.now())+' Id Anime: {}'.format(pk))
    animes = get_object_or_404(Bank, pk=pk)
    opc = ListaUser.objects.filter(user_id=request.user.id, anime_id=pk).exists()

    if opc == True:
        task = get_object_or_404(ListaUser, user_id=request.user.id, anime_id=pk)
        form = PostForm(instance=task)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=task)

            if form.is_valid():
                task.save()
                print('Alteração de Anime na Galeria do Usuário: '+request.user.username+' '+str(datetime.datetime.now())+' Id Anime: {}'.format(pk))
                return redirect('/')

            else:
                return render(request, 'meusite/animes.html', {'animes' : animes, 'form': form})
        else:
            return render(request, 'meusite/animes.html', {'animes' : animes, 'form': form})
    else:
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST)
            
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.anime = Bank.objects.get(pk=pk)
                task.save()
                print('Adição de Anime na Galeria do Usuário: '+request.user.username+' '+str(datetime.datetime.now())+' Id Anime: {}'.format(pk))
                return redirect('/')
        else:
            form = PostForm()
            return render(request, 'meusite/animes.html', {'animes' : animes, 'form': form})

def catalogo(request):
    print('Acesso ao Catálogo: '+request.user.username+' '+str(datetime.datetime.now()))
    bank = Bank.objects.all()
    return render(request, 'meusite/catalogo.html', {'bank':bank})

def contatos(request):
    print('Acesso ao Contato: '+request.user.username+' '+str(datetime.datetime.now()))
    dice = {}
    if request.method == 'POST':
        dice['nome'] = request.POST.get('nome')
        dice['email'] = request.POST.get('email')
        dice['type'] = request.POST.get('type')
        dice['mensagem'] = request.POST.get('mensagem')

        send_mail(
            dice['nome'],
            'Remetente: ' + dice['email'] + '\n\n' + 'Tipo do Contato: ' + dice['type'] + '\n\n' + dice['mensagem'],
            '',
            # [settings.EMAIL_HOST_USER],
            [settings.EMAIL_BACKEND],
        )
        print('Envio de Mensagem de Contato: Remetente '+dice['email']+' '+str(datetime.datetime.now()))
        return redirect('/')
    return render(request, 'meusite/contatos.html', dice)

def sobre(request):
    print('Acesso a Sobre: '+request.user.username+' '+str(datetime.datetime.now()))
    return render(request, 'meusite/sobre.html')

@login_required
def profile(request, pk):
    print('Acesso a Galeria: Usuário '+request.user.username+' '+str(datetime.datetime.now()))
    animess = ListaUser.objects.filter(user_id=pk)
    animes = Bank.objects.filter(id__in={instance.anime_id for instance in animess})
    return render(request, 'meusite/user.html', {'animes' : animes})


def view_404(request, exception):
    print('Erro: '+request.user.username+' '+str(datetime.datetime.now()))
    bank = Bank.objects.all()
    return render(request, 'meusite/index.html', {'bank':bank})

def delete(request, pk):
    opc = ListaUser.objects.filter(user_id=request.user.id, anime_id=pk).exists()

    if opc == True:
        task = get_object_or_404(ListaUser, user_id=request.user.id, anime_id=pk)
        task.delete()
        print('Remoção de Anime da Galeria: Usuário '+request.user.username+' '+str(datetime.datetime.now())+' Id Anime: {}'.format(pk))
        return redirect('/')
    else:
        return render(request, 'meusite/user.html', {'animes' : animes})