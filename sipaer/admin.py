# -*- encoding: utf-8 -*-
from django.contrib import admin
from notificacao.models import Ocorrencia, Aeronave, Fator, Lesao, Tripulacao, AeronaveDetalhe, FatorContribuicao, Pais, Uf, Cidade, Aerodromo, Violacao, ViolacaoDetalhe, Documento

class CidadeAdmin(admin.ModelAdmin):
    list_display = ('cidade',)

class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'equipamento', 'fabricante', 'modelo', 'categoria')
    search_fields = ('matricula','equipamento')
    list_filter = ('categoria',)
    ordering = ('categoria',)
    #fields = ('matricula', 'equipamento', 'fabricante', 'modelo', 'categoria')

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('documento','status_documento')

class FatorAdmin(admin.ModelAdmin):
    list_display = ('area','nome_fator')
    search_fields = ('nome_fator', 'area')
    ordering = ('area',)

class FatorContribuicaoAdmin(admin.ModelAdmin):
    list_display = ('latente','nivel_contribuicao',)
    ordering = ('latente','nivel_contribuicao',)

class FatorContribuicaoInline(admin.TabularInline):
    model = FatorContribuicao
    extra = 0

class ViolacaoAdmin(admin.ModelAdmin):
    list_display = ('area','tipo')
    search_fields = ('tipo', 'area')
    ordering = ('area',)

class ViolacaoDetalheAdmin(admin.ModelAdmin):
    list_display = ('violacao','detalhe',)
    ordering = ('violacao','detalhe',)

class ViolacaoDetalheInline(admin.TabularInline):
    model = ViolacaoDetalhe
    extra = 0

class TripulacaoAdmin(admin.ModelAdmin):
    list_display = ('codigo_anac','funcao')
    ordering = ('nome',)

class TripulacaoInline(admin.TabularInline):
    model = Tripulacao
    extra = 0

class LesaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_lesao','quantidade')
    search_fields = ('tipo_lesao','quantidade')
    ordering = ('quantidade',)

class LesaoInline(admin.TabularInline):
    model = Lesao
    extra = 0

class AeronaveDetalheAdmin(admin.ModelAdmin):
    list_display = ('aeronave','operador', 'fase_voo')
    ordering = ('operador',)
    inlines = [LesaoInline,TripulacaoInline,]

class AeronaveDetalheInline(admin.StackedInline):
    model = AeronaveDetalhe
    extra = 0
    inlines = [LesaoInline,TripulacaoInline]
    #readonly_fields = ('changeform_link', )

class DocumentoInline(admin.TabularInline):
    model = Documento
    extra = 0

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('classificacao','tipo','aerodromo','dia')
    search_fields = ('classificacao','aerodromo')
    list_filter = ('classificacao','tipo','dia')
    #ordering = ('dia',)
    #date_hierarchy = 'dia'
    #ERRO#raw_id_fields = ('lesao',)
    inlines = [DocumentoInline,AeronaveDetalheInline, FatorContribuicaoInline, ViolacaoDetalheInline,]

# Register your models here.
admin.site.register(Pais)
admin.site.register(Uf)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Aerodromo)
admin.site.register(Aeronave, AeronaveAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Fator, FatorAdmin)
admin.site.register(Violacao, ViolacaoAdmin)
admin.site.register(Lesao, LesaoAdmin)
admin.site.register(Tripulacao, TripulacaoAdmin)
admin.site.register(AeronaveDetalhe, AeronaveDetalheAdmin)
admin.site.register(FatorContribuicao, FatorContribuicaoAdmin)
admin.site.register(ViolacaoDetalhe, ViolacaoDetalheAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)

#FIM ADMIN
