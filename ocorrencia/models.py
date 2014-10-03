# -*- coding: UTF-8 -*-
from django.db import models


from django.db import models
from django.contrib.auth.models import User
from ocorrencia.taxonomia import *
from treinamento.models import Aluno

#INICIO MODEL
#LOCALIDADE
class Pais(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome do país', unique=True)
    nome_codigo = models.CharField(max_length=3, verbose_name='Código do país', unique=True)
    idioma_codigo = models.CharField(max_length=3, verbose_name='Idioma Principal')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'
        ordering = ['nome']
    def save(self):
        self.nome = self.nome.upper()
        self.nome_codigo = self.nome_codigo.upper()
        self.idioma_codigo = self.idioma_codigo.upper()
        super(Pais, self).save()

class Uf(models.Model):
    pais = models.ForeignKey(Pais, verbose_name='País')
    nome = models.CharField(max_length=30, default = 'EXTERIOR', verbose_name='Nome do Estado/Província')
    nome_codigo = models.CharField(max_length=3, default = 'EX', verbose_name='Código do Estado/Província')
    regiao = models.CharField(max_length=20, choices = UfTaxonomia.REGIAO, verbose_name='Região geográfica')
    comar = models.CharField(max_length=10, choices = UfTaxonomia.COMAR, verbose_name='COMAR dessa região')
    def __str__(self):
        nome_codigo = self.nome_codigo
        codigo_pais = self.pais.nome_codigo
        return nome_codigo + ' | ' + codigo_pais
    class Meta:
        verbose_name = 'UF'
        verbose_name_plural = 'UFs'
        unique_together = (('pais','nome'),)
        ordering = ['nome']
    def save(self):
        self.nome = self.nome.upper()
        self.nome_codigo = self.nome_codigo.upper()
        self.regiao = self.regiao.upper()
        self.comar = self.comar.upper()
        super(Uf, self).save()

class Cidade(models.Model):
    uf = models.ForeignKey(Uf, null=True, verbose_name='Estado')
    pais = models.ForeignKey(Pais, verbose_name='País')
    nome = models.CharField(max_length=100, verbose_name='Cidade')
    def __str__(self):
        return self.nome  + ' | ' + self.uf.nome_codigo + ' | ' + self.pais.nome_codigo
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        unique_together = (('uf','pais','nome'),)
    def save(self):
        self.nome = self.nome.upper()
        super(Cidade, self).save()
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "nome__icontains",)


#AERODROMO
class Aerodromo(models.Model):
    cidade = models.ForeignKey(Cidade, verbose_name='Localidade')
    icao = models.CharField(max_length=4, verbose_name='Código ICAO', unique=True)
    iata = models.CharField(max_length=3, verbose_name='Código IATA', default='***')
    nome = models.CharField(max_length=100, verbose_name='Nome do Aeródromo', null=True)
    propriedade = models.CharField(max_length=10, choices = AerodromoTaxonomia.PROPRIEDADE, verbose_name='Propriedade')
    tipo = models.CharField(max_length=12, choices = AerodromoTaxonomia.TIPO, verbose_name='Tipo')
    latitude = models.CharField(max_length=15, verbose_name='Latitude', blank=True)
    longitude = models.CharField(max_length=15, verbose_name='Longitude', blank=True)
    altitude = models.FloatField(verbose_name='Altitude', null=True)
    vfr_diurno = models.CharField(max_length=5, choices = OutrosTaxonomia.SIMNAO, verbose_name='VFR diurno')
    vfr_noturno = models.CharField(max_length=5, choices = OutrosTaxonomia.SIMNAO, verbose_name='VFR noturno')
    ifr_diurno = models.CharField(max_length=5, choices = OutrosTaxonomia.SIMNAO, verbose_name='IFR diurno')
    ifr_noturno = models.CharField(max_length=5, choices = OutrosTaxonomia.SIMNAO, verbose_name='IFR noturno')
    def __str__(self):
        return self.icao # + ' | ' + self.cidade.nome
    class Meta:
        verbose_name = 'Aeródromo'
        verbose_name_plural = 'Aeródromos'
    def save(self):
        self.icao = self.icao.upper()
        self.iata = self.iata.upper()
        self.nome = self.nome.upper()
        super(Aerodromo, self).save()
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "icao__icontains",)


class AerodromoPista(models.Model):
    aerodromo = models.ForeignKey(Aerodromo, verbose_name='Aerodromo')
    nome = models.CharField(max_length=50, verbose_name='Nome da Pista')
    comprimento = models.FloatField(verbose_name='Comprimento', null=True)
    largura = models.FloatField(verbose_name='Largura', null=True)
    cabeceira_a = models.CharField(max_length=5, verbose_name='Cabeceira A', null=True)
    cabeceira_b = models.CharField(max_length=5, verbose_name='Cabeceira B', null=True)
    piso = models.CharField(max_length=20, choices = AerodromoPistaTaxonomia.PISO, verbose_name='Piso')
    pcn = models.IntegerField(verbose_name='PCN', null=True)
    pavimento = models.CharField(max_length=3, choices = AerodromoPistaTaxonomia.PAVIMENTO, verbose_name='Pavimento')
    resist_subleito = models.CharField(max_length=3, choices = AerodromoPistaTaxonomia.RESISTSUBLEITO, verbose_name='Resistência do subleito')
    pressao_maxima = models.CharField(max_length=3, choices = AerodromoPistaTaxonomia.PRESMAXIMA, verbose_name='Pressão máxima')
    avaliacao_pcn = models.CharField(max_length=3, choices = AerodromoPistaTaxonomia.AVALIAPCN, verbose_name='Avaliação do PCN')
    pmpa_kg = models.FloatField(verbose_name='PMPA (kg)', null=True)
    pmp_mpa = models.FloatField(verbose_name='PMP (mpa)', null=True)
    pista_formato = models.CharField(max_length=12, choices = AerodromoPistaTaxonomia.PISTAFORMATO, verbose_name='Formato da Pista/Heliponto')
    def __str__(self):
        return self.aerodromo.icao + ' | ' + self.nome
    class Meta:
        verbose_name = 'Pista'
        verbose_name_plural = 'Pistas'
    def save(self):
        self.nome = self.nome.upper()
        super(AerodromoPista, self).save()



#OCORRÊNCIA
class Ocorrencia(models.Model):
    cidade = models.ForeignKey(Cidade, verbose_name='Localidade da Ocorrência')
    aerodromo = models.ForeignKey(Aerodromo, related_name='aerodromo_ocorrencia', verbose_name='Aeródromo da Ocorrência')
    latitude = models.CharField(max_length=15, verbose_name='Latitude', default='***', blank=True)
    longitude = models.CharField(max_length=15, verbose_name='Longitude', default='***', blank=True)
    numero_processo = models.CharField(max_length=30, verbose_name='Nº Processo', unique=True)
    classificacao = models.CharField(max_length=20, choices=OcorrenciaTaxonomia.CLASSIFOCORRENCIA,  verbose_name='Classificação')
    tipo = models.CharField(max_length=100,choices=OcorrenciaTaxonomia.TIPOCORRENCIA, verbose_name='Tipo de Ocorrência')
    dia = models.DateField(verbose_name='Dia')
    horario = models.TimeField(verbose_name='Horário')
    danos_terceiros = models.CharField(max_length=10, choices=OutrosTaxonomia.SIMNAO, verbose_name='Danos a Terceiros')
    historico = models.TextField(max_length=2500, verbose_name='Histórico da Ocorrência', null=True)
    cadastrado_por = models.ForeignKey(User, null=True, verbose_name='Cadastrado por', related_name='cadastrado_por')
    cadastrado_em = models.DateField(auto_now_add=True, verbose_name='Cadastrado em')
    def __str__(self):
        return self.classificacao + ' | ' + self.numero_processo
    class Meta:
        verbose_name = 'Ocorrência'
        verbose_name_plural = 'Ocorrências'
    def save(self):
        self.historico = self.historico.upper()
        super(Ocorrencia, self).save()

#FATORES CONTRIBUINTES
class Fator(models.Model):
    area = models.CharField(max_length = 20, choices = FatorTaxonomia.AREA, verbose_name='Área do Fator')
    aspecto = models.CharField(max_length= 20, choices = FatorTaxonomia.ASPECTO, verbose_name='Aspecto do Fator')
    condicionante = models.CharField(max_length = 50, choices = FatorTaxonomia.CONDICIONANTE, verbose_name='Condicionante')
    nome = models.CharField(max_length = 50, verbose_name='Nome do Fator', unique=True)
    nome_codigo = models.CharField(max_length = 10, verbose_name='Código do Fator', unique=True)
    def __str__(self):
        fator = self.nome
        area = self.area
        return fator + ' | ' + area
    class Meta:
        verbose_name = 'Fator'
        verbose_name_plural = 'Fatores'
    def save(self):
        self.nome = self.nome.upper()
        self.nome_codigo = self.nome_codigo.upper()
        super(Fator, self).save()

class FatorOcorrencia(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, verbose_name='Ocorrência')
    fator = models.ForeignKey(Fator, verbose_name='Fator Contribuinte')
    nivel_contribuicao = models.CharField(max_length = 20, choices=FatorOcorrenciaTaxonomia.NIVELCONTRIBUICAO, verbose_name='Nível de Contribuição')
    relatorio = models.CharField(max_length = 20, choices = FatorOcorrenciaTaxonomia.RELATORIO, verbose_name='Relatório')
    observacao = models.CharField(max_length = 200, verbose_name='Observações')
    def __str__(self):
        nome_fator = self.fator.nome
        contribuicao = self.nivel_contribuicao
        return nome_fator + ' | ' + contribuicao
    class Meta:
        verbose_name = 'Fator Contribuinte'
        verbose_name_plural = 'Fatores Contribuintes'
    def save(self):
        self.observacao = self.observacao.upper()
        super(FatorOcorrencia, self).save()

#AERONAVES ENVOLVIDAS NA OCORRÊNCIA
class Aeronave(models.Model):
    matricula = models.CharField(max_length=10, verbose_name='Matrícula', unique=True)
    nacionalidade_registro = models.ForeignKey(Pais, related_name='estado_registro', verbose_name='Estado de Registro')
    nacionalidade_fabricacao = models.ForeignKey(Pais, related_name='estado_fabricacao', verbose_name='Estado de Fabricação')
    ano_fabricacao = models.IntegerField(max_length=4, blank=True, verbose_name='Ano de Fabricação')
    classificacao = models.CharField(max_length=10, choices=AeronaveTaxonomia.CLASSIFICACAO, default='CIVIL', verbose_name='Classificação da Aeronave')
    equipamento = models.CharField(max_length=10, choices=AeronaveTaxonomia.EQUIPAMENTO, verbose_name='Equipamento')
    fabricante_codigo = models.CharField(max_length = 3, default='***', verbose_name='Código do Fabricante')
    fabricante_nome = models.CharField(max_length = 50, default='***', verbose_name='Fabricante')
    modelo = models.CharField(max_length = 50, default='***', verbose_name='Modelo')
    classe =  models.CharField(max_length = 3, choices=AeronaveTaxonomia.CLASSE, verbose_name='Classe')
    tipo_icao =  models.CharField(max_length = 5, verbose_name='Tipo ICAO', default='***')
    tipo_motor = models.CharField(max_length=10, choices=AeronaveTaxonomia.TIPOMOTOR, verbose_name='Motor')
    quantidade_motor = models.IntegerField(blank=True, verbose_name='Quantidade de Motores')
    tipo_trem_pouso = models.CharField(max_length=10, choices=AeronaveTaxonomia.TIPOTREMPOUSO, verbose_name='Trem de Pouso')
    numero_assentos = models.IntegerField(blank=True, verbose_name='Assentos')
    numero_serie =  models.CharField(max_length = 15, default='***', verbose_name='Número de Série')
    passageiros_maximo = models.IntegerField(blank=True, verbose_name='Max. Passageiros')
    peso_max_decolagem = models.FloatField(blank=True, verbose_name='Peso Max. Decolagem')
    tipo_certificado = models.CharField(max_length = 15, default='***', verbose_name='Certificado ANAC')
    tripulacao_minima = models.IntegerField(blank=True, verbose_name='Trip. Mínima')
    def __str__(self):
        return self.matricula + ' | ' + self.equipamento
    class Meta:
        verbose_name = 'Aeronave'
        verbose_name_plural = 'Aeronaves'
    def save(self):
        self.matricula = self.matricula.upper()
        self.fabricante_codigo = self.fabricante_codigo.upper()
        self.fabricante_nome = self.fabricante_nome.upper()
        self.modelo = self.modelo.upper()
        self.classe = self.classe.upper()
        self.tipo_icao = self.tipo_icao.upper()
        self.numero_serie = self.numero_serie.upper()
        self.tipo_certificado = self.tipo_certificado.upper()
        super(Aeronave, self).save()

class AeronaveCategoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Categoria', unique=True)
    nome_codigo = models.CharField(max_length=3, verbose_name='Código da Categoria', unique=True)
    regulamento = models.CharField(max_length=40, choices=AeronaveCategoriaTaxonomia.REGULAMENTO, verbose_name='Regulamento', default='***')
    aviacao = models.CharField(max_length=15, choices=AeronaveCategoriaTaxonomia.AVIACAO, verbose_name='Tipo da Aviação', default='***')
    def __str__(self):
        return self.nome_codigo
    class Meta:
        verbose_name = 'Aeronave Categoria'
        verbose_name_plural = 'Aeronave Categorias'
    def save(self):
        self.nome = self.nome.upper()
        self.nome_codigo = self.nome_codigo.upper()
        super(AeronaveCategoria, self).save()

class AeronaveFaseVoo(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Fase', unique=True)
    nome_codigo = models.CharField(max_length=6, verbose_name='Código da Fase')
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Aeronave Fase Voo'
        verbose_name_plural = 'Aeronave Fase Voo'
    def save(self):
        self.nome = self.nome.upper()
        self.nome_codigo = self.nome_codigo.upper()
        super(AeronaveFaseVoo, self).save()

class AeronaveOcorrencia(models.Model):
    aeronave = models.ForeignKey(Aeronave, verbose_name='Matrícula da Aeronave')
    ocorrencia = models.ForeignKey(Ocorrencia, verbose_name='Ocorrência')
    origem_voo = models.ForeignKey(Aerodromo, related_name='origem_voo', verbose_name='Origem do Voo', null=True)
    destino_voo = models.ForeignKey(Aerodromo, related_name='destino_voo', verbose_name='Destino do Voo', null=True)
    categoria = models.ForeignKey(AeronaveCategoria, verbose_name='Categoria de Registro')
    operador = models.CharField(max_length=100, verbose_name='Operador da Aeronave')
    operacao = models.CharField(max_length=45, choices=AeronaveOcorrenciaTaxonomia.OPERACAO, verbose_name='Tipo de Operação')
    fase_voo = models.ForeignKey(AeronaveFaseVoo, verbose_name='Fase de Voo')
    danos = models.CharField(max_length=15, choices=AeronaveOcorrenciaTaxonomia.DANOS, verbose_name='Nível do Dano')
    custo_reparo = models.FloatField(max_length=20, null=True, blank=True, verbose_name='Custo do Reparo')
    observacoes = models.CharField(max_length=200, verbose_name='Observações', blank=True)
    def __str__(self):
        return self.aeronave.matricula #+ ' | ' + self.ocorrencia + ' | ' + self.operador
    class Meta:
        verbose_name = 'Aeronave Envolvida'
        verbose_name_plural = 'Aeronaves Envolvidas'
    def save(self):
        self.operador = self.operador.upper()
        self.observacoes = self.observacoes.upper()
        super(AeronaveOcorrencia, self).save()

'''

#DADOS DO NOTIFICANTE
class NotificanteOcorrencia(models.Model):
    ocorrencia = models.OneToOneField(Ocorrencia)
    emitido_por = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nome do Notificante')
    data_notificacao = models.DateField(auto_created=True, editable=False, auto_now=True, verbose_name='Data')
    email_notificante = models.EmailField(verbose_name='Email para contato')
    telefone_notificante = models.CharField(max_length=20, blank=False, null=False, verbose_name='Telefone para contato')
    observacoes = models.TextField(max_length=500, blank=True, null=True, verbose_name='Observações')
    def __str__(self):
        return self.emitido_por
    class Meta:
        verbose_name = 'Notificante'
        verbose_name_plural = 'Dados do Notificante'

#APOIO
class OcorrenciaApoio(models.Model):
    ocorrencia = models.OneToOneField(Ocorrencia, verbose_name='Ocorrência')
    confirmado_por = models.ForeignKey(User, blank=True, null=True, verbose_name='Confirmado por', related_name='confirmado_por')
    autenticado_por = models.ForeignKey(User, blank=True, null=True, verbose_name='Autenticado por', related_name='autenticado_por')
    diretorio_dop = models.CharField(max_length=45, verbose_name='Endereço na rede')
    publicado_site = models.BooleanField(verbose_name='Publicado no site?')
    observacoes = models.CharField(max_length=500, verbose_name='Observações')
    def __str__(self):
        return self.ocorrencia + ' | ' + self.diretorio_dop
    class Meta:
        verbose_name = 'Informações de apoio'
        verbose_name_plural = 'Informações de apoio'

#CONTROLE DA INVESTIGAÇÃO
class ControleInvestigacao(models.Model):
    ocorrencia = models.OneToOneField(Ocorrencia, verbose_name='Ocorrência')
    decisao = models.CharField(max_length=45, choices=InvestigacaoTaxonomia.DECISAO,  verbose_name='Ocorrência investigada?')
    comando_investigador = models.CharField(max_length=12, choices=InvestigacaoTaxonomia.COMANDOINVESTIGADOR,  verbose_name='Comando Investigador')
    investigador_responsavel = models.ForeignKey(Aluno, verbose_name='Investigador Responsável')
    situacao_investigacao = models.CharField(max_length=20, choices=InvestigacaoTaxonomia.SITUACAO,  verbose_name='Situação da Investigação')
    revisado_cenipa = models.CharField(max_length=10, choices=OutrosTaxonomia.SIMNAO, default='NÃO',  verbose_name='RF/SUMA revisado pelo CENIPA')
    custo_investigacao = models.FloatField(max_length=20, null=True, blank=True, verbose_name='Custo da Investigação')
    ultima_fase = models.CharField(max_length=20, choices=InvestigacaoTaxonomia.ULTIMAFASE,  verbose_name='Última fase da Ocorrência')
    final_investigacao = models.DateField(verbose_name='Última fase da Investigação')
    observacoes = models.CharField(max_length=500, verbose_name='Observações')
    def __str__(self):
        return self.ocorrencia + ' | ' + self.comando_investigador
    class Meta:
        verbose_name = 'Controle da Investigação'
        verbose_name_plural = 'Controle da Investigação'

#DOCUMENTOS
class Documento(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, verbose_name='Ocorrência')
    tipo = models.CharField(max_length=50, choices=DocumentoTaxonomia.TIPO,  verbose_name='Tipo de Documento')
    numero = models.CharField(max_length=30, verbose_name='Número')
    despacho = models.CharField(max_length=45, choices=DocumentoTaxonomia.DESPACHO,  verbose_name='Tipo de Despacho')
    origem_destino = models.CharField(max_length=50, verbose_name='Origem/Destino')
    data = models.DateField(verbose_name='Data de Entrada/Saída')
    situacao = models.CharField(max_length=45, choices=DocumentoTaxonomia.SITUACAO,  verbose_name='Status')
    observacoes = models.CharField(max_length=500, verbose_name='Observações')
    def __str__(self):
        return self.tipo + ' | ' + self.numero + ' | ' + self.situacao
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

#DESTINATARIOS DE RECOMENDACOES/DIVULGACAO
class DestinatarioRecomendacao(models.Model):
    nome_destinatario = models.CharField(max_length=25, verbose_name='Nome do Destinatário')
    def __str__(self):
        return self.nome_destinatario
    class Meta:
        verbose_name = 'Destinatário da Divulgação'
        verbose_name_plural = 'Destinatários da Divulgação'

#RECOMENDACOES DE SEGURANCA
class RecomendacaoSeguranca(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia)
    aplicacao = models.CharField(max_length=20, choices=RecomendacaoSegurancaTaxonomia.APLICACAO, verbose_name='Aplicação')
    numero = models.CharField(max_length=25, verbose_name='Numeração')
    dia_emissao = models.DateField(verbose_name='Data da Emissão')
    destinatario_recomendacao = models.ForeignKey(DestinatarioRecomendacao, default='ANAC', verbose_name='Destinatário')
    texto_recomendacao = models.TextField(max_length=1000, verbose_name='Recomendação de Segurança')
    dia_feedback = models.DateField(verbose_name='Data do Feedback')
    numero_documento_feedback = models.CharField(max_length=25, verbose_name='Número do Doc. Feedback')
    situacao_recomendacao = models.CharField(max_length=10, choices=RecomendacaoSegurancaTaxonomia.SITUACAO, verbose_name='Cumprimento da Recomendação', default = 'AGUARDANDO RESPOSTA')
    observacoes_cumprimento = models.TextField(max_length=1000, verbose_name='Observações Referentes ao Cumprimento')
    def __str__(self):
        return self.numero + ' | ' + self.destinatario_recomendacao
    class Meta:
        verbose_name = 'Recomendação de Segurança'
        verbose_name_plural = 'Recomendações de Segurança'

#DIVULGAÇÃO DE RECOMENDACOES
class DivulgacaoRecomendacao(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia)
    destinatario_divulgacao = models.ForeignKey(DestinatarioRecomendacao, default='ANAC', verbose_name='Destinatário')
    numero_encaminhamento = models.CharField(max_length=25, verbose_name='Número do Encaminhamento')
    dia_encaminhamento = models.DateField(verbose_name='Data do Encaminhamento')
    def __str__(self):
        return self.destinario
    class Meta:
        verbose_name = 'Divulgação de Recomendação'
        verbose_name_plural = 'Divulgação de Recomendações'

#ASSUNTOS INTERNACIONAIS
class AssuntosInternacionais(models.Model):
    ocorrencia = models.OneToOneField(Ocorrencia, verbose_name='Ocorrência')
    rep_acreditado = models.CharField(max_length=10, choices=OutrosTaxonomia.SIMNAO, verbose_name='Tem Rep. Acreditado')
    adrep = models.CharField(max_length=10, choices=OutrosTaxonomia.SIMNAO, verbose_name='Envio de ADREP')
    numero_adrep = models.CharField(max_length=30, verbose_name='Número do ADREP', blank=True)
    class Meta:
        verbose_name = 'Assuntos Internacionais'
        verbose_name_plural = 'Assuntos Internacionais'

class NotificacaoRC(models.Model):
    assunto_internacional = models.ForeignKey(AssuntosInternacionais)
    destino = models.CharField(max_length=50, verbose_name='Destino')
    fabricante_aeronave = models.CharField(max_length=50, verbose_name='Modelo de Aeronave')
    modelo_aeronave = models.CharField(max_length=50, verbose_name='Modelo de Aeronave')
    estado = models.ForeignKey(Pais, related_name='uf_notificacao_rc', verbose_name='Estado')
    iic = models.CharField(max_length=50, verbose_name='Investigator in Charge')
    accrep = models.CharField(max_length=50, verbose_name='Accredited Representative')
    email_accrep = models.EmailField(verbose_name='Accredited Representative E-mail')
    pr_icao = models.CharField(max_length=50)
    draft_rf_ra = models.CharField(max_length=50)
    recebimento_draft = models.CharField(max_length=50)
    envio_adrep_icao = models.CharField(max_length=50)
    def __str__(self):
        return self.destino + ' | ' + self.modelo_aeronave
    class Meta:
        verbose_name = 'Notificação ASOACI'
        verbose_name_plural = 'Notificações ASOACI'




'''
#LESÕES NA AERONAVE
class Lesao(models.Model):
    tipo_lesao = models.CharField(max_length = 50, choices=LesoesTaxonomia.TIPO)
    pessoa = models.CharField(max_length=15, choices=LesoesTaxonomia.PESSOA)
    quantidade = models.IntegerField()
    aeronave_detalhe = models.ForeignKey(AeronaveOcorrencia)
    def __str__(self):
        return self.tipo_lesao
    class Meta:
        verbose_name = 'Lesão'
        verbose_name_plural = 'Lesões'
'''
#TRIPULAÇÃO DA AERONAVE
class Tripulante(models.Model):
    codigo_anac = models.CharField(max_length=10, unique=True, verbose_name='Número do Documento')
    orgao_expedidor = models.CharField(max_length=15, verbose_name='Órgão Expedidor')
    nome_tripulante = models.CharField(max_length=150, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    nacionalidade = models.CharField(max_length=60, verbose_name='Nacionalidade do Tripulante')
    escola_formacao = models.CharField(max_length=50, verbose_name='Escola de Formação')
    ano_formacao = models.CharField(max_length=4, verbose_name='Ano de Formação')
    cht_pessoa = models.CharField(max_length=50, verbose_name='Tipos de CHT')
    tipo_curso = models.CharField(max_length=50, verbose_name='Tipo de Curso Realizado')
    sexo_tripulante = models.CharField(max_length=12, choices=OutrosTaxonomia.SEXO, verbose_name='Sexo do Tripulante')
    def __str__(self):
        return self.codigo_anac
    class Meta:
        verbose_name = 'Tripulante'
        verbose_name_plural = 'Tripulantes'

class TripulanteAeronave(models.Model):
    funcao = models.CharField(max_length=30, choices=TripulacaoTaxonomia.FUNCAOTRIPULANTE, verbose_name='Função do Tripulante')
    total_horas_voo = models.FloatField(verbose_name='Horas de Voo (total)')
    horas_voo_modelo = models.FloatField(verbose_name='Horas de Voo (modelo)')
    horas_voo_ultimos_30d = models.FloatField(verbose_name='Horas de Voo (últimos 30 dias)')
    horas_voo_ultimas_24h = models.FloatField(verbose_name='Horas de Voo (últimas 24 horas)')
    status_vida = models.CharField(max_length=10, choices=OutrosTaxonomia.SIMNAO, verbose_name='Sobreviveu')
    aeronave_detalhe = models.ForeignKey(AeronaveDetalhe)
    tripulante = models.ForeignKey(Tripulante)
    def __str__(self):
        return self.funcao
    class Meta:
        verbose_name = 'Tripulante na Aeronave'
        verbose_name_plural = 'Tripulantes na Aeronave'

#ASSESSORIA JURIDICA
class DemandaJuridica(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, verbose_name='Ocorrência')
    data_solicitacao = date
    data_resposta = date
    orgao_solicitante = char
    processo_relacionado = char
    informacao_solicitada = text
    informacao_prestada = text
    situacao = char
    observacoes = models.CharField(max_length=500, verbose_name='Observações')
    def __str__(self):
        return self.ocorrencia + ' | ' + self.numero + ' | ' + self.situacao
    class Meta:
        verbose_name = 'Demanda Judicial'
        verbose_name_plural = 'Demandas Judiciais'


#VIOLAÇÕES
class Violacao(models.Model):
    tipo = models.CharField(max_length=50, verbose_name='Tipo da Violação', unique=True)
    tipo_codigo = models.CharField(max_length=30, verbose_name='Código da Violação')
    area = models.CharField(max_length=50, verbose_name='Área da Violação')
    area_codigo = models.CharField(max_length=30, verbose_name='Código da Área')
    def __str__(self):
        return self.tipo
    class Meta:
        verbose_name = 'Violação'
        verbose_name_plural = 'Violações'

class ViolacaoDetalhe(models.Model):
    ocorrencia = models.ForeignKey(Ocorrencia, verbose_name='Ocorrência')
    violacao = models.ForeignKey(Violacao, verbose_name='Violação')
    observacoes = models.CharField(max_length=50, verbose_name='Observações')
    class Meta:
        verbose_name = 'Violação na Ocorrência'
        verbose_name_plural = 'Violações na Ocorrência'

#FIM MODEL
'''