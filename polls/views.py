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

def matematica1ef(request):
    return render(request, 'polls/matematica1ef.html')


