from django.contrib import admin

from .models import Alternativa, Pergunta


class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 3

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['texto_pergunta']}),
        ('Date information', {'fields': ['data_publicacao'], 'classes': ['collapse']}),
    ]
    inlines = [AlternativaInline]
    list_display = ('texto_pergunta', 'data_publicacao', 'publicada_recente')
    list_filter = ['data_publicacao']
    search_fields = ['texto_pergunta']

admin.site.register(Pergunta, PerguntaAdmin)




