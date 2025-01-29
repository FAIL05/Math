from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from .models import Usuario
from django.shortcuts import get_object_or_404, render


def index(request):
    latest_question_list = Usuario.objects.all()
    context = {"lastest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def login(request):
   return render(request, 'polls/login.html')

def cadastro(request):
    return render(request, 'polls/cadastro.html')
    
def mathquest(request):
    return render(request, 'polls/mathquest.html')

def perfil(request):
    return render(request, 'polls/perfil.html')

def sobre(request):
    return render(request, 'polls/sobre.html')


def matematicaef1(request):
    return render(request, 'polls/matematicaef1.html')

def matematicaef2(request):
    return render(request, 'polls/matematicaef2.html')

def matematicaef3(request):
    return render(request, 'polls/matematicaef3.html')

def matematicaef4(request):
    return render(request, 'polls/matematicaef4.html')

def matematicaef5(request):
    return render(request, 'polls/matematicaef5.html')

def matematicaef6(request):
    return render(request, 'polls/matematicaef6.html')

def matematicaef7(request):
    return render(request, 'polls/matematicaef7.html')

def matematicaef8(request):
    return render(request, 'polls/matematicaef8.html')

def matematicaef9(request):
    return render(request, 'polls/matematicaef9.html')