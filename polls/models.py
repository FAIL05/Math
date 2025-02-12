from django.db import models
from django.utils import timezone
import datetime

class Usuario(models.Model):
    nome = models.CharField (max_length=100)
    email = models.EmailField (max_length=100, unique=True)
    senha = models.CharField (max_length=100)
 
    def __str__ (self):
        return self.nome
        
class Pergunta (models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField('data de publicação')

    def __str__(self):
        return self.texto_pergunta
    
    def publicada_recente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.data_publicacao <=now

    publicada_recente.admin_order_field = 'data_publicacao'
    publicada_recente.boolean = True
    publicada_recente.short_description = 'Publicação recente?'

class Alternativa (models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_alternativa
    


    




