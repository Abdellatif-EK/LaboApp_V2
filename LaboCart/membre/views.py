from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
from membre.models import Utilisateur,Analyste
from .forms import  AnalysteForm


def index(request):
    return render(request, 'authentification/administration.html',{
        'Utilisateurs': Analyste.objects.all()
    })

def add(request):
    if request.method == 'POST':
        form = AnalysteForm(request.POST)
        if form.is_valid():
            new_analyste_first_name = form.cleaned_data["first_name"]
            new_analyste_last_name = form.cleaned_data["last_name"]
            new_analyste_email = form.cleaned_data["email"]
            new_analyste_password = form.cleaned_data["password"]
            new_analyste_phone = form.cleaned_data["phone"]

            new_analyste = Analyste(
                first_name=new_analyste_first_name, 
                last_name=new_analyste_last_name, 
                email=new_analyste_email, 
                password=new_analyste_password, 
                phone=new_analyste_phone
            )
            new_analyste.save()
            return render(request, 'authentification/ajout.html',{
                'form':AnalysteForm(),
                'success': True
            })
    else:
        form = AnalysteForm()
    return render(request, 'authentification/ajout.html', {'form': AnalysteForm()})

def update(request, id):
    if request.method == 'POST' :
        analyste = Analyste.objects.get(pk=id)
        form = AnalysteForm(request.POST, instance=analyste)
        if form.is_valid():
            form.save()
            return redirect(request, 'authentification/modifier.html',{
                'from' : form,
                'success': True
            })
    else:
        analyste = Analyste.objects.get(pk=id)
        form = AnalysteForm(instance=analyste)

def connexion(request):
    if request.method == "POST":
        username = request.POST["utilisateur"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,("Il y a eu une erreur lors de la connexion, essai encore!"))
            return redirect('connexion')
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'authentification/login.html')

@login_required
def deconnexion(request):
    logout(request)
    messages.success(request,("Vous avez été deconnecté!"))
    return redirect('connexion')

@login_required
def user_creat(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username, password=password)
            messages.success(request, ("l'utilisateur crée"))
            return redirect('adminn')    
    else:
        form = UserCreationForm()

    return render(request, 'authentification/creation.html', {"form":form,})

@login_required
def administrer(request):
    return render(request, 'authentification/administration.html')




