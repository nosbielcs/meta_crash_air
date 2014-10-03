# -*- coding: UTF-8 -*-
from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome Completo")
    sexo = models.BooleanField()
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Curso(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.ForeignKey(Curso)
    alunos = models.ManyToManyField(Aluno)
    def __str__(self):
        return self.nome

class TurmaAluno(models.Model):
    aluno = models.ForeignKey(Aluno)
    turma = models.ForeignKey(Turma)
    def __str__(self):
        return "Turma: %s | Aluno: %s" % (self.turma, self.aluno)


# Create your models here.
