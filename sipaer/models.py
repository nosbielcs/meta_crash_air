# -*- encoding: utf-8 -*-
from django.db import models
from notificacao.taxonomia import ClassificacaoTaxonomia, AeronaveTaxonomia, ComandoTaxonomia, FatorContribuicaoTaxonomia, SimNaoTaxonomia, DocumentoTaxonomia, StatusDocumentoTaxonomia, SituacaoTaxonomia
from django.contrib.auth.models import User

class Pais(models.Model):
    pais = models.CharField(max_length=50)
    def __str__(self):
        return self.pais
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'

class Uf(models.Model):
    uf_nome = models.CharField(max_length=100, null=True)
    uf_codigo = models.CharField(max_length=2, null=True)
    def __str__(self):
        return self.uf_codigo
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.ForeignKey(Uf, null=True)
    pais = models.ForeignKey(Pais)
    def __str__(self):
        return self.cidade + ' - ' + self.uf.uf_codigo + ' - ' + self.pais.pais
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'

class Aerodromo(models.Model):
    icao = models.CharField(max_length=20)
    iata = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade)
    def __str__(self):
        return self.icao + ' - ' + self.cidade.cidade
    class Meta:
        verbose_name = 'Aeródromo'
        verbose_name_plural = 'Aeródromos'

class Aeronave(models.Model):
    matricula = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=30)
    categoria = models.CharField(max_length=3)
    equipamento = models.CharField(max_length=25)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=45)
    tipo_motor = models.CharField(max_length=50)
    quantidade_motor = models.IntegerField()
    trem_pouso = models.CharField(max_length=45)
    classificacao = models.CharField(max_length=45)
    ano_fabricacao = models.IntegerField()
    def __str__(self):
        return self.matricula + ' - ' + self.categoria
    class Meta:
        verbose_name = 'Aeronave'
        verbose_name_plural = 'Aeronaves'

class Fator(models.Model):
    area = models.CharField(max_length = 20)
    aspecto = models.CharField(max_length= 20)
    condicionante = models.CharField(max_length = 50)
    nome_fator = models.CharField(max_length = 50)
    def __str__(self):
        fator = self.nome_fator
        area = self.area
        return fator + ' - ' + area
    class Meta:
        verbose_name = 'Fator'
        verbose_name_plural = 'Fatores'

class Violacao(models.Model):
    tipo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = 'Violação'
        verbose_name_plural = 'Violações'

class Ocorrencia(models.Model):
    classificacao = models.CharField(max_length=20, choices=ClassificacaoTaxonomia.CLASSIFICACAO, default='-')
    tipo = models.CharField(max_length=100)
    dia = models.DateField()
    horario = models.TimeField()
    comando_investigador = models.CharField(max_length=12, choices=ComandoTaxonomia.COMANDO, default='-')
    origem = models.ForeignKey(Aerodromo, related_name='origem_voo')
    destino = models.ForeignKey(Aerodromo, related_name='destino_voo')
    aerodromo = models.ForeignKey(Aerodromo, related_name='aerodromo_voo')
    cidade = models.ForeignKey(Cidade)
    situacao = models.CharField(max_length=45, choices=SituacaoTaxonomia.SITUACAO, default='-')
    danos_terceiros = models.CharField(max_length=10, choices=SimNaoTaxonomia.SIMNAO, default = '-')
    historico = models.TextField(max_length=2500)
    def __str__(self):
        return self.classificacao
    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'

class Documento(models.Model):
    documento = models.CharField(max_length=50, choices=DocumentoTaxonomia.DOCUMENTO, default='-')
    status_documento = models.CharField(max_length=45, choices=StatusDocumentoTaxonomia.DOCUMENTOSTATUS, default='-')
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ocorrencia = models.ForeignKey(Ocorrencia)
    def __str__(self):
        return self.documento + self.status_documento
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

class AeronaveDetalhe(models.Model):
    operador = models.CharField(max_length=100)
    operacao = models.CharField(max_length=45)
    fase_voo = models.CharField(max_length=60)
    danos = models.CharField(max_length=15, choices=AeronaveTaxonomia.DANOS, default = '-')
    aeronave = models.ForeignKey(Aeronave)
    ocorrencia = models.ForeignKey(Ocorrencia)
    def __str__(self):
        return self.operador
    class Meta:
        verbose_name = 'Aeronave Envolvida'
        verbose_name_plural = 'Aeronaves Envolvidas'

class FatorContribuicao(models.Model):
    fator = models.ForeignKey(Fator)
    nivel_contribuicao = models.CharField(max_length = 20, choices=FatorContribuicaoTaxonomia.FATORCONTRIBUINTE, default = '-')
    latente = models.BooleanField()
    ocorrencia = models.ForeignKey(Ocorrencia)
    class Meta:
        verbose_name = 'Fator Contribuinte'
        verbose_name_plural = 'Fatores Contribuintes'

class Lesao(models.Model):
    tipo_lesao = models.CharField(max_length = 50)
    pessoa = models.CharField(max_length=15)
    quantidade = models.IntegerField()
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)
    def __str__(self):
        return self.tipo_lesao
    class Meta:
        verbose_name = 'Lesão'
        verbose_name_plural = 'Lesões'

class Tripulacao(models.Model):
    codigo_anac = models.IntegerField()
    funcao = models.CharField(max_length=30)
    nome = models.CharField(max_length=60)
    orgao_expedidor = models.CharField(max_length=15)
    total_horas_voo = models.FloatField()
    horas_voo_modelo = models.FloatField(max_length=3)
    horas_voo_ultimos_30d = models.FloatField()
    horas_voo_ultimas_24h = models.FloatField()
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Tripulante'
        verbose_name_plural = 'Tripulantes'

class ViolacaoDetalhe(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia)
    violacao = models.ForeignKey(Violacao)
    detalhe = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Violação na Ocorrência'
        verbose_name_plural = 'Violações na Ocorrência'

#FIM MODEL
