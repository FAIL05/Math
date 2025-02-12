from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from .models import Usuario
from django.views import generic
from django.utils import timezone
from django.shortcuts import get_object_or_404, render

from .models import Pergunta, Alternativa

class IndexView(generic.ListView):
    template_name = 'polls/lista.html'
    context_object_name = 'lista_ultimas_perguntas'

    def get_queryset(self):
        return Pergunta.objects.filter(
            data_publicacao__lte=timezone.now()
        ).order_by('-data_publicacao')[:5]
    
class DetailView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/detalhe.html'

    def get_queryset(self):
        return Pergunta.objects.filter(data_publicacao__lte=timezone.now())
    
class ResultsViews(generic.DetailView):
    model = Pergunta
    template_name = 'polls/resultados.html'

def votar(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        alternativa_selecionada = pergunta.alternativa_set.get(pk=request.POST['alternativa'])

    except (KeyError, Alternativa.DoesNotExist):
        return render (request, 'polls/detalhe.html', {
            'pergunta': pergunta,
            'error_message': "Você não selecionou nenhuma alternativa",
        })
    else:
        alternativa_selecionada.votos += 1
        alternativa_selecionada.save()
        return HttpResponseRedirect(reverse('polls:resultados', args=(pergunta.id,)))
        


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

def password_reset_form(request):
    return render(request, 'polls/password_reset_form.html')
