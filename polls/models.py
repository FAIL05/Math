from django.db import models
#

class Usuario(models.Model):
    nome = models.CharField (max_length=100)
    email = models.EmailField (max_length=100, unique=True)
    senha = models.CharField (max_length=100)
    data_nascimento = models.DateField (max_length=100)
    foto_perfil = models.ImageField (upload_to='polls/imagens')

    def __str__ (self):
        return self.nome
        

class Question (models.Model):
    enunciado = models.CharField (max_length=500)
    topico = models.CharField (max_length=500)
    tipo_questao = models.CharField (max_length=500)

    def __str__ (self):
        return self.enunciado
        

class Respostas (models.Model):
    tipo_questao = models.CharField (max_length=500)
    resposta_fornecida = models.CharField (max_length=500)

    id_usuarios = models.ForeignKey (Usuario, on_delete=models.CASCADE)
    id_questões = models.ForeignKey (Question, on_delete=models.CASCADE)

    def __str__ (self):
        return self.resposta_fornecida


class Opções_de_Resposta (models.Model):
    descricao = models.CharField (max_length=500)
    correta = models.BooleanField (blank=False)

    def __str__(self):
        return self.correta


class Material_de_Estudo (models.Model):
    descricao = models.CharField (max_length=500)
    link = models.CharField (max_length=500)

    def __str__ (self):
        return self.link
    



