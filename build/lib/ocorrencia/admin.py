# -*- coding: UTF-8 -*-
#from django.utils.encoding import force_unicode
from django.contrib import admin
from grappelli_nested.admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline
from ocorrencia.models import *
from django.forms import ModelForm, TextInput
#from suit.widgets import SuitDateWidget, SuitTimeWidget, AutosizedTextarea, LinkedSelect, EnclosedInput, Select, HTML5Input

#CONFIGURACOES GERAIS
#admin.site.disable_action('delete_selected')



#LOCALIDADE
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome','uf','pais')
    list_filter = ('nome','uf','pais',)
    search_fields = ['nome',]
    ordering =('nome',)
    autocomplete_lookup_fields = {'fk': ['cidade',],}


#AERODROMO
class AerodromoPistaAdmin(admin.ModelAdmin):
    list_display = ('aerodromo','nome','comprimento','largura','piso','pavimento','pista_formato','cabeceira_a','cabeceira_b')
    list_filter = ('aerodromo','nome','comprimento','largura','piso','pavimento',)
    search_fields = ('nome',)

class AerodromoPistaInline(admin.StackedInline):
    model = AerodromoPista
    extra = 0

class AerodromoAdmin(admin.ModelAdmin):
    list_display = ('icao','iata','cidade','nome','propriedade','tipo','altitude')
    list_filter = ('icao','iata','cidade__nome','cidade__uf__nome','nome','propriedade','tipo',)
    search_fields = ('nome','icao',)
    inlines = [AerodromoPistaInline,]

#FATORES CONTRIBUINTES
class FatorAdmin(admin.ModelAdmin):
    list_display = ('area', 'aspecto', 'condicionante', 'nome', 'nome_codigo')
    list_filter = ('area', 'aspecto', 'condicionante', 'nome' )
    ordering = ('area',)

class FatorOcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('ocorrencia', 'fator', 'nivel_contribuicao', 'relatorio')
    list_filter = ('fator', 'nivel_contribuicao','ocorrencia')
    ordering = ('nivel_contribuicao',)

class FatorOcorrenciaInline(admin.TabularInline):
    model = FatorOcorrencia
    extra = 0

#AERONAVE
class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'equipamento', 'fabricante_nome', 'modelo','ano_fabricacao')
    search_fields = ('matricula',)
    list_filter = ('equipamento','modelo','ano_fabricacao')
    ordering = ('ano_fabricacao',)

class AeronaveCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_codigo', 'regulamento', 'aviacao')
    list_filter = ('nome', 'nome_codigo', 'regulamento', 'aviacao')
    ordering = ('nome',)

class AeronaveFaseVooAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_codigo')
    list_filter = ('nome', 'nome_codigo')
    ordering = ('nome',)


'''
#VIOLACAO
class ViolacaoAdmin(admin.ModelAdmin):
    list_display = ('area', 'tipo')
    list_filter = ('tipo', 'area')
    ordering = ('area',)

class ViolacaoDetalheAdmin(admin.ModelAdmin):
    list_display = ('ocorrencia', 'violacao', 'observacoes')
    list_filter = ('ocorrencia__classificacao','ocorrencia','violacao','violacao__area')
    ordering = ('violacao','observacoes',)

class ViolacaoDetalheInline(admin.TabularInline):
    model = ViolacaoDetalhe
    extra = 0

#TRIPULACAO
#class TripulanteAdmin(admin.ModelAdmin):
class TripulanteAdmin(NestedModelAdmin):
    list_display = ('nome_tripulante',)
    list_filter = ('nome_tripulante',)

#class TripulanteInline(admin.StackedInline):
class TripulanteInline(NestedStackedInline):
    model = Tripulante
    extra = 0

#class TripulanteAeronaveAdmin(admin.ModelAdmin):
class TripulanteAeronaveAdmin(NestedModelAdmin):
    list_display = ('funcao','tripulante','aeronave_detalhe')
    list_filter = ('funcao','tripulante','aeronave_detalhe')
    ordering = ('funcao',)

#class TripulanteAeronaveInline(admin.StackedInline):
class TripulanteAeronaveInline(NestedStackedInline):
    model = TripulanteAeronave
    extra = 0
'''
#LESAO
#class LesaoAdmin(admin.ModelAdmin):
class LesaoAdmin(NestedModelAdmin):
    list_display = ('aeronave_detalhe','tipo_lesao','pessoa', 'quantidade')
    list_filter = ('aeronave_detalhe__ocorrencia__classificacao', 'aeronave_detalhe__aeronave','tipo_lesao','pessoa')
    ordering = ('quantidade',)

#class LesaoInline(admin.TabularInline):
class LesaoInline(NestedTabularInline):
    model = Lesao
    extra = 1

#AERONAVES ENVOLVIDAS
class AeronaveOcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('aeronave','ocorrencia','categoria','operador', 'fase_voo')
    list_filter = ('aeronave','ocorrencia','categoria','operador', 'fase_voo')
    ordering = ('ocorrencia__dia',)
    #inlines = [LesaoInline,TripulanteAeronaveInline,]

#class AeronaveOcorrenciaInline(admin.StackedInline):
class AeronaveOcorrenciaInline(NestedStackedInline):
    model = AeronaveOcorrencia
    extra = 1
    inlines = [LesaoInline,]
    #inlines = [LesaoInline,TripulanteAeronaveInline]
    #readonly_fields = ('changeform_link', )

'''
#DOCUMENTOS
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('tipo','origem_destino','despacho','data')
    list_filter = ('tipo','origem_destino')
    ordering = ('data',)
    date_hierarchy = 'data'

class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 0

#ASSUNTOS INTERNACIONAIS
class NotificacaoRCAdmin(admin.ModelAdmin):
#class NotificacaoRCAdmin(NestedModelAdmin):
    list_display = ('destino','modelo_aeronave')
    list_filter = ('destino','modelo_aeronave','accrep',)

class NotificacaoRCInline(admin.StackedInline):
#class NotificacaoRCInline(NestedTabularInline):
    model = NotificacaoRC
    extra = 0

class AssuntosInternacionaisAdmin(admin.ModelAdmin):
#class AssuntosInternacionaisAdmin(NestedModelAdmin):
    list_display = ('ocorrencia','rep_acreditado','adrep','numero_adrep')
    list_filter = ('ocorrencia','rep_acreditado','adrep','numero_adrep')
    inlines = [NotificacaoRCInline,]

class AssuntosInternacionaisInline(admin.TabularInline):
#class AssuntosInternacionaisInline(NestedTabularInline):
    model = AssuntosInternacionais
    extra = 0
    inlines = [NotificacaoRCInline,]

#RECOMENDACAO DE SEGURANÇA
class RecomendacaoSegurancaAdmin(admin.ModelAdmin):
    list_display = ('ocorrencia','aplicacao','numero','situacao_recomendacao')
    list_filter = ('ocorrencia','aplicacao','numero','situacao_recomendacao')

class RecomendacaoSegurancaInline(admin.StackedInline):
    model = RecomendacaoSeguranca
    extra = 0

#DIVULGACAO DE RECOMENDACAO DE SEGURANÇA
class DivulgacaoRecomendacaoAdmin(admin.ModelAdmin):
    pass

class DivulgacaoRecomendacaoInline(admin.TabularInline):
    model = DivulgacaoRecomendacao
    extra = 0

#NOTIFICANTE DA OCORRENCIA
class NotificanteOcorrenciaAdmin(admin.ModelAdmin):
    pass

class NotificanteOcorrenciaInline(admin.TabularInline):
    model = NotificanteOcorrencia
    extra = 1

#CONTROLE DA INVESTIGAÇÃO
class ControleInvestigacaoAdmin(admin.ModelAdmin):
    pass

class ControleInvestigacaoInline(admin.StackedInline):
    model = ControleInvestigacao
    extra = 1
'''
#OCORRENCIA
#class OcorrenciaAdmin(admin.ModelAdmin):
class OcorrenciaAdmin(NestedModelAdmin):
    list_display = ('numero_processo','classificacao','tipo','cidade','aerodromo','dia','horario')
    search_fields = ['classificacao', 'aerodromo__icao', 'dia']
    list_filter = ['classificacao','tipo', 'cidade', 'danos_terceiros']
    ordering = ('-cadastrado_em',)
    raw_id_fields = ('cidade','aerodromo',)
    autocomplete_lookup_fields = {'fk': ['cidade','aerodromo'],}
    date_hierarchy = 'dia'
    inlines = [AeronaveOcorrenciaInline, ]
    #ERRO#raw_id_fields = ('lesao',)
    #inlines = [AeronaveOcorrenciaInline, NotificanteOcorrenciaInline, ControleInvestigacaoInline, DocumentoInline, FatorOcorrenciaInline, ViolacaoDetalheInline, AssuntosInternacionaisInline, RecomendacaoSegurancaInline, DivulgacaoRecomendacaoInline]


# Register your models here.
admin.site.register(Pais)
admin.site.register(Uf)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(AerodromoPista, AerodromoPistaAdmin)
admin.site.register(Aerodromo, AerodromoAdmin)
admin.site.register(Fator, FatorAdmin)
admin.site.register(FatorOcorrencia, FatorOcorrenciaAdmin)
admin.site.register(Aeronave, AeronaveAdmin)
admin.site.register(AeronaveCategoria, AeronaveCategoriaAdmin)
admin.site.register(AeronaveFaseVoo, AeronaveFaseVooAdmin)
admin.site.register(AeronaveOcorrencia, AeronaveOcorrenciaAdmin)
#admin.site.register(Documento, DocumentoAdmin)
#admin.site.register(Violacao, ViolacaoAdmin)
admin.site.register(Lesao, LesaoAdmin)
#admin.site.register(Tripulante, TripulanteAdmin)
#admin.site.register(TripulanteAeronave, TripulanteAeronaveAdmin)
#admin.site.register(ViolacaoDetalhe, ViolacaoDetalheAdmin)
#admin.site.register(NotificacaoRC, NotificacaoRCAdmin)
#admin.site.register(AssuntosInternacionais, AssuntosInternacionaisAdmin)
#admin.site.register(DestinatarioRecomendacao)
#admin.site.register(RecomendacaoSeguranca, RecomendacaoSegurancaAdmin)
#admin.site.register(DivulgacaoRecomendacao, DivulgacaoRecomendacaoAdmin)
#admin.site.register(NotificanteOcorrencia, NotificanteOcorrenciaAdmin)
#admin.site.register(ControleInvestigacao, ControleInvestigacaoAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)


#FIM ADMIN
