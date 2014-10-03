# -*- coding: UTF-8 -*-

from django.contrib import admin
from treinamento.models import Aluno, Curso, Turma, TurmaAluno

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','sexo',)
    list_filter = ('nome','sexo',)
    search_fields = ('nome','sexo',)

class AlunoInline(admin.TabularInline):
    model = Aluno
    extra = 0

class TurmaAdmin(admin.ModelAdmin):
    filter_horizontal = ('alunos',)

class TurmaAlunoAdmin(admin.ModelAdmin):
    list_display = ('turma','aluno',)

class TurmaInline(admin.TabularInline):
    model = Turma
    extra = 0

class CursoAdmin(admin.ModelAdmin):
    inlines = [TurmaInline,]

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(TurmaAluno)
