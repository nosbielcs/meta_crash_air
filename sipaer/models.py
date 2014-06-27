from django.db import models
from sipaer.taxonomia import ClassificacaoTaxonomia, AeronaveTaxonomia, ComandoTaxonomia
import datetime

# Create your models here.

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

class Fator(models.Model):
    area = models.CharField(max_length = 20)
    aspecto = models.CharField(max_length= 20)
    condicionante = models.CharField(max_length = 50)
    nome_fator = models.CharField(max_length = 50)
    def __str__(self):
        fator = self.nome_fator
        area = self.area
        return area + ' - ' + fator

class Ocorrencia(models.Model):
    classificacao = models.CharField(max_length=20, choices=ClassificacaoTaxonomia.CLASSIFICACAO, default='-')
    tipo = models.CharField(max_length=100)
    dia = models.DateTimeField('Data da Ocorrência:')
    comando_investigador = models.CharField(max_length=12, choices=ComandoTaxonomia.COMANDO, default='-')
    aerodromo = models.CharField(max_length=25)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
    pais = models.CharField(max_length=30)
    documento = models.CharField(max_length=50)
    situacao = models.CharField(max_length=45)
    status_documento = models.CharField(max_length=45)
    danos_terceiros = models.CharField(max_length=10)
    historico = models.TextField(max_length=2500)
    def __str__(self):
        return self.classificacao

class AeronaveDetalhe(models.Model):
    operador = models.CharField(max_length=100)
    operacao = models.CharField(max_length=45)
    fase_voo = models.CharField(max_length=60)
    danos = models.CharField(max_length=15, choices=AeronaveTaxonomia.DANOS, default = '-')
    aeronave = models.ForeignKey(Aeronave)
    ocorrencia = models.ForeignKey(Ocorrencia)

    '''def changeform_link(self):
        if self.id:
            # Replace "myapp" with the name of the app containing
            # your Certificate model:
            changeform_url = urlresolvers.reverse(
                'admin:sipaer_aeronavedetalhe_change', args=(self.id,)
                )
            return u'<a href="%s" target="_blank">Detalhes</a>' % changeform_url
        return u''
    changeform_link.allow_tags = True
    changeform_link.short_description = 'Lesoes'   # omit column header'''

    def __str__(self):
        return self.operador

class FatorContribuicao(models.Model):
    nivel_contribuicao = models.CharField(max_length = 20)
    ocorrencia = models.ForeignKey(Ocorrencia)
    fator = models.ForeignKey(Fator)

class Lesao(models.Model):
    tipo_lesao = models.CharField(max_length = 50)
    pessoa = models.CharField(max_length=15)
    quantidade = models.IntegerField()
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)

    def __str__(self):
        return self.tipo_lesao

class Tripulacao(models.Model):
    codigo_anac = models.IntegerField()
    funcao = models.CharField(max_length=30)
    nome = models.CharField(max_length=60)
    orgao_expedidor = models.CharField(max_length=15)
    total_horas_voo = models.FloatField()
    horas_voo_modelo = models.FloatField()
    horas_voo_ultimos_30d = models.FloatField()
    horas_voo_ultimas_24h = models.FloatField()
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)
    def __str__(self):
        return self.nome





