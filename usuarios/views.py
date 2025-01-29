from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import UsuarioPersonalizadoCreationForm, UsuarioPersonalizadoAuthenticationForm

# Create your views here.
def cadastro(request):
    form = UsuarioPersonalizadoCreationForm()
    if request.method == 'POST':
        form = UsuarioPersonalizadoCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('polls:mathquest')

        print("Metodo GEt")
        
    else:
        form = UsuarioPersonalizadoCreationForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

     
def login_usuario (request):
    if request.method == 'POST':
        form = UsuarioPersonalizadoAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate (request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('polls:mathquest')
    else:
        form = UsuarioPersonalizadoAuthenticationForm()
        return render(request, 'usuarios/login.html', {'form': form})
   
def sair (request):
    logout(request)
    return redirect('usuarios:login')
       


