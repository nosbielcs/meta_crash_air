from django.contrib import admin
from sipaer.models import Ocorrencia, Aeronave, Fator, Lesao, Tripulacao, AeronaveDetalhe, FatorContribuicao

class AeronaveAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'equipamento', 'fabricante', 'modelo', 'categoria')
    search_fields = ('matricula','equipamento')
    list_filter = ('categoria',)
    ordering = ('categoria',)
    #fields = ('matricula', 'equipamento', 'fabricante', 'modelo', 'categoria')

class FatorAdmin(admin.ModelAdmin):
    list_display = ('area','nome_fator')
    search_fields = ('nome_fator', 'area')
    ordering = ('area',)

class FatorContribuicaoAdmin(admin.ModelAdmin):
    list_display = ('nivel_contribuicao',)
    ordering = ('nivel_contribuicao',)

class FatorContribuicaoInline(admin.TabularInline):
    model = FatorContribuicao
    extra = 1

class TripulacaoAdmin(admin.ModelAdmin):
    list_display = ('codigo_anac','funcao')
    ordering = ('nome',)

class TripulacaoInline(admin.TabularInline):
    model = Tripulacao
    extra = 1

class LesaoAdmin(admin.ModelAdmin):
    list_display = ('tipo_lesao','quantidade')
    search_fields = ('tipo_lesao','quantidade')
    ordering = ('quantidade',)

class LesaoInline(admin.TabularInline):
    model = Lesao
    extra = 1

class AeronaveDetalheAdmin(admin.ModelAdmin):
    list_display = ('aeronave','operador', 'fase_voo')
    ordering = ('operador',)
    inlines = [LesaoInline,TripulacaoInline,]

class AeronaveDetalheInline(admin.StackedInline):
    model = AeronaveDetalhe
    extra = 1
    inlines = [LesaoInline,TripulacaoInline]
    #readonly_fields = ('changeform_link', )

class OcorrenciaAdmin(admin.ModelAdmin):
    list_display = ('classificacao','tipo','aerodromo','dia')
    search_fields = ('classificacao','aerodromo')
    list_filter = ('classificacao','tipo','dia')
    #ordering = ('dia',)
    #date_hierarchy = 'dia'
    #ERRO#raw_id_fields = ('lesao',)
    inlines = [AeronaveDetalheInline, FatorContribuicaoInline,]

# Register your models here.
admin.site.register(Aeronave, AeronaveAdmin)
admin.site.register(Fator, FatorAdmin)
admin.site.register(Lesao, LesaoAdmin)
admin.site.register(Tripulacao, TripulacaoAdmin)
admin.site.register(AeronaveDetalhe, AeronaveDetalheAdmin)
admin.site.register(FatorContribuicao, FatorContribuicaoAdmin)
admin.site.register(Ocorrencia, OcorrenciaAdmin)
