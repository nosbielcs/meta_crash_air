from django.db import models
from sipaer.taxonomia import ClassificacaoTaxonomia, AeronaveTaxonomia, ComandoTaxonomia, FatorContribuicao

class Pais(models.Model):
    pais = models.CharField(max_length=50)
    def __str__(self):
        return self.pais

class Uf(models.Model):
    uf_nome = models.CharField(max_length=100, null=True)
    uf_codigo = models.CharField(max_length=2, null=True)
    def __str__(self):
        return self.uf

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)
    uf = models.ForeignKey(Uf, null=True)
    pais = models.ForeignKey(Pais)
    def __str__(self):
        return self.cidade + ' - ' + self.uf.uf_codigo + ' - ' + self.pais.pais

class Aerodromo(models.Model):
    icao = models.CharField(max_length=10)
    iata = models.CharField(max_length=10)
    cidade = models.ForeignKey(Cidade)

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
    dia = models.DateField()
    horario = models.TimeField()
    comando_investigador = models.CharField(max_length=12, choices=ComandoTaxonomia.COMANDO, default='-')
    origem = models.CharField(max_length=25)
    destino = models.CharField(max_length=25)
    aerodromo = models.ForeignKey(Aerodromo)
    cidade = models.ForeignKey(Cidade)
    #uf = models.CharField(max_length=2)
    #pais = models.CharField(max_length=30)
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
    def __str__(self):
        return self.operador

class FatorContribuicao(models.Model):
    fator = models.ForeignKey(Fator)
    nivel_contribuicao = models.CharField(max_length = 20, choices=FatorContribuicao.TAXONOMIA, default = '-')
    latente = models.BooleanField()
    ocorrencia = models.ForeignKey(Ocorrencia)

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
    horas_voo_modelo = models.FloatField(max_length=3)
    horas_voo_ultimos_30d = models.FloatField()
    horas_voo_ultimas_24h = models.FloatField()
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)
    def __str__(self):
        return self.nome

class Violacao(models.Model):
    tipo = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    def __str__(self):
        return self.tipo

class ViolacaoDetalhe(models.Model):
    detalhe = models.CharField(max_length=200)
    ocorrencia = models.ForeignKey(Ocorrencia)
    violacao = models.ForeignKey(Violacao)
	
#FIM MODEL