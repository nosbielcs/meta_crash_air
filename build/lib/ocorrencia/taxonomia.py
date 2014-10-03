# -*- coding: UTF-8 -*-
############################################
#GERAL TAXONOMIA
############################################
class OutrosTaxonomia():
    #SIM NAO
    TALVEZ = '***'
    SIM = 'SIM'
    NAO = 'NÃO'
    SIMNAO = (
        (TALVEZ, '***'),
        (NAO, 'NÃO'),
        (SIM, 'SIM')
    )

    #SEXO
    M = 'MASCULINO'
    F = 'FEMININO'
    SEXO = (
        (M, 'MASCULINO'),
        (F, 'FEMININO')
    )

############################################
#UF TAXONOMIA
############################################
class UfTaxonomia():
    #REGIAO
    REG1 = '***'
    REG2 = 'FORA DO BRASIL'
    REG3 = 'CENTRO-OESTE'
    REG4 = 'NORDESTE'
    REG5 = 'NORTE'
    REG6 = 'SUDESTE'
    REG7 = 'SUL'
    REGIAO = (
        (REG1 , '***'),
        (REG2 , 'FORA DO BRASIL'),
        (REG3 , 'CENTRO-OESTE'),
        (REG4 , 'NORDESTE'),
        (REG5 , 'NORTE'),
        (REG6 , 'SUDESTE'),
        (REG7 , 'SUL')
    )

    #COMAR
    FORA_COMAR = '***'
    COMAR1 = 'COMAR-1'
    COMAR2 = 'COMAR-2'
    COMAR3 = 'COMAR-3'
    COMAR4 = 'COMAR-4'
    COMAR5 = 'COMAR-5'
    COMAR6 = 'COMAR-6'
    COMAR7 = 'COMAR-7'
    COMAR = (
        (FORA_COMAR , '***'),
        (COMAR1 , 'COMAR-1'),
        (COMAR2 , 'COMAR-2'),
        (COMAR3 , 'COMAR-3'),
        (COMAR4 , 'COMAR-4'),
        (COMAR5 , 'COMAR-5'),
        (COMAR6 , 'COMAR-6'),
        (COMAR7 , 'COMAR-7')
    )

############################################
#AERODROMO TAXONOMIA
############################################
class AerodromoTaxonomia():
    #PROPRIEDADE
    PROP1 = '***'
    PROP2 = 'PRIVADO'
    PROP3 = 'PÚBLICO'
    PROPRIEDADE = (
        (PROP1 , '***'),
        (PROP2 , 'PRIVADO'),
        (PROP3 , 'PÚBLICO')
    )

    #TIPO AERODROMO
    TAEROD1 = '***'
    TAEROD2 = 'AERÓDROMO'
    TAEROD3 = 'CLAREIRA'
    TAEROD4 = 'HELIDECK'
    TAEROD5 = 'HELIPONTO'
    TIPO = (
        (TAEROD1 , '***'),
        (TAEROD2 , 'AERÓDROMO'),
        (TAEROD3 , 'CLAREIRA'),
        (TAEROD4 , 'HELIDECK'),
        (TAEROD5 , 'HELIPONTO')
    )

############################################
#AERODROMO PISTA TAXONOMIA
############################################
class AerodromoPistaTaxonomia():
    #PISO
    PISO1 = '***'
    PISO2 = 'AÇO'
    PISO3 = 'AREIA'
    PISO4 = 'ARGILA'
    PISO5 = 'ASFALTO'
    PISO6 = 'CASCALHO'
    PISO7 = 'CONCRETO'
    PISO8 = 'GRAMA'
    PISO9 = 'MADEIRA'
    PISO10 = 'METÁLICO'
    PISO11 = 'NÃO DEFINIDO'
    PISO12 = 'PARALELEPÍPEDO'
    PISO13 = 'PIÇARRA'
    PISO14 = 'SAIBRO'
    PISO15 = 'TERRA'
    PISO = (
        (PISO1 , '***'),
        (PISO2 , 'AÇO'),
        (PISO3 , 'AREIA'),
        (PISO4 , 'ARGILA'),
        (PISO5 , 'ASFALTO'),
        (PISO6 , 'CASCALHO'),
        (PISO7 , 'CONCRETO'),
        (PISO8 , 'GRAMA'),
        (PISO9 , 'MADEIRA'),
        (PISO10 , 'METÁLICO'),
        (PISO11 , 'NÃO DEFINIDO'),
        (PISO12 , 'PARALELEPÍPEDO'),
        (PISO13 , 'PIÇARRA'),
        (PISO14 , 'SAIBRO'),
        (PISO15 , 'TERRA')
    )

    #PAVIMENTO
    PAV1 = '***'
    PAV2 = 'F'
    PAV3 = 'R'
    PAVIMENTO = (
        (PAV1 , '***'),
        (PAV2 , 'F'),
        (PAV3 , 'R')
    )

    #RESISTENCIA SUBLEITO
    RESS1 = '***'
    RESS2 = 'A'
    RESS3 = 'B'
    RESS4 = 'C'
    RESS5 = 'D'
    RESISTSUBLEITO = (
        (RESS1 , '***'),
        (RESS2 , 'A'),
        (RESS3 , 'B'),
        (RESS4 , 'C'),
        (RESS5 , 'D')
    )

    #PRESSAO MAXIMA
    PRESS1 = '***'
    PRESS2 = 'X'
    PRESS3 = 'Y'
    PRESS4 = 'Z'
    PRESS5 = 'W'
    PRESMAXIMA = (
        (PRESS1 , '***'),
        (PRESS2 , 'X'),
        (PRESS3 , 'Y'),
        (PRESS4 , 'Z'),
        (PRESS5 , 'W')
    )

    #AVALIACAO_PCN
    AVPCN1 = '***'
    AVPCN2 = 'T'
    AVPCN3 = 'U'
    AVALIAPCN = (
        (AVPCN1 , '***'),
        (AVPCN2 , 'T'),
        (AVPCN3 , 'U')
    )

    #PISTA FORMATO
    PISTFORMAT1 = '***'
    PISTFORMAT2 = 'CIRCULAR'
    PISTFORMAT3 = 'OCTOGONAL'
    PISTFORMAT4 = 'QUADRADO'
    PISTFORMAT5 = 'RETANGULAR'
    PISTAFORMATO = (
        (PISTFORMAT1 , '***'),
        (PISTFORMAT2 , 'CIRCULAR'),
        (PISTFORMAT3 , 'OCTOGONAL'),
        (PISTFORMAT4 , 'QUADRADO'),
        (PISTFORMAT5 , 'RETANGULAR')
    )

############################################
#OCORRENCIA TAXONOMIA
############################################
class OcorrenciaTaxonomia():
    #CLASSIFICACAO
    ANALISE = '***'
    ACIDENTE = 'ACIDENTE'
    INCIDENTE_GRAVE = 'INCIDENTE GRAVE'
    INCIDENTE = 'INCIDENTE'
    ANORMAL = 'ANORMAL'
    TRAFEGO_AEREO = 'TRÁFEGO AEREO'
    OC_SOLO = 'OC. DE SOLO'
    CLASSIFOCORRENCIA = (
        (ANALISE, '***'),
        (ACIDENTE, 'ACIDENTE'),
        (INCIDENTE_GRAVE, 'INCIDENTE GRAVE'),
        (INCIDENTE, 'INCIDENTE'),
        (ANORMAL, 'ANORMAL'),
        (TRAFEGO_AEREO, 'TRÁFEGO AEREO'),
        (OC_SOLO, 'OC. DE SOLO')
    )

    #TIPO DE OCORRÊNCIA
    TIPOC1	= 'AERONAVE ATINGIDA POR OBJETO'
    TIPOC2	= 'ALARME FALSO OU SUPERAQUECIMENTO'
    TIPOC3	= 'CAUSADO POR FENOMENO METEOROLÓGICO EM VOO'
    TIPOC4	= 'CAUSADO POR FENOMENO METEOROLÓGICO NO SOLO'
    TIPOC5	= 'CAUSADO POR RICOCHETE'
    TIPOC6	= 'CFIT'
    TIPOC7	= 'COLISÃO COM AERONAVE NO SOLO'
    TIPOC8	= 'COLISÃO COM OBSTÁCULO NO SOLO'
    TIPOC9	= 'COLISÃO COM PÁSSARO'
    TIPOC10	= 'COLISÃO DE AERONAVES EM VOO'
    TIPOC11	= 'COLISÃO DE VEÍCULO COM AERONAVE'
    TIPOC12	= 'COLISÃO EM VOO COM OBJETO REBOCADO'
    TIPOC13	= 'COM CANOPI'
    TIPOC14	= 'COM COMANDOS DE VOO'
    TIPOC15	= 'COM HÉLICE'
    TIPOC16	= 'COM LANÇAMENTO OU TRANSPORTE DE CARGA'
    TIPOC17	= 'COM LANÇAMENTO OU TRANSPORTE DE PESSOAS'
    TIPOC18	= 'COM PÁRA-BRISAS/JANELA/PORTA'
    TIPOC19	= 'COM PESSOAL EM VOO'
    TIPOC20	= 'COM ROTOR'
    TIPOC21	= 'COM TREM DE POUSO'
    TIPOC22	= 'COM TURBINA'
    TIPOC23	= 'CORTE INVOLUNTÁRIO DO MOTOR'
    TIPOC24	= 'DE TRÁFEGO AÉREO'
    TIPOC25	= 'DESCOMPRESSÃO NÃO INTENCIONAL / EXPLOSIVA'
    TIPOC26	= 'DESORIENTAÇÃO ESPACIAL / ATITUDE ANORMAL'
    TIPOC27	= 'DISPARO INVOLUNTÁRIO DE ARMAMENTO'
    TIPOC28	= 'EJEÇÃO INVOLUNTÁRIA'
    TIPOC29	= 'ESTOURO DE PNEU'
    TIPOC30	= 'EXCURSÃO DE PISTA'
    TIPOC31	= 'EXPLOSÃO'
    TIPOC32	= 'EXPOSIÇÃO A SUBSTÂNCIA TÓXICA'
    TIPOC33	= 'F.O.D.'
    TIPOC34	= 'FALHA DE SISTEMA / COMPONENTE'
    TIPOC35	= 'FALHA DO MOTOR EM VOO'
    TIPOC36	= 'FALHA DO MOTOR NO SOLO'
    TIPOC37	= 'FALHA ESTRUTURAL'
    TIPOC38	= 'FOGO EM VOO'
    TIPOC39	= 'FOGO NO SOLO'
    TIPOC40	= 'FUMAÇA'
    TIPOC41	= 'FUMAÇA NA CABINE'
    TIPOC42	= 'INCIDENTE C/ HÉLICE/ ROTOR / TURBINA'
    TIPOC43	= 'INCURSÃO EM PISTA'
    TIPOC44	= 'INDETERMINADA'
    TIPOC45	= 'INDICAÇÃO FALSA DE INSTRUMENTO'
    TIPOC46	= 'MANOBRAS A BAIXA ALTURA'
    TIPOC47	= 'OUTROS TIPOS'
    TIPOC48	= 'PANE SECA'
    TIPOC49	= 'PERDA DA CONSCIÊNCIA'
    TIPOC50	= 'PERDA DE COMPONENTE EM VOO'
    TIPOC51	= 'PERDA DE COMPONENTE NO SOLO'
    TIPOC52	= 'PERDA DE CONTROLE EM VOO'
    TIPOC53	= 'PERDA DE CONTROLE NO SOLO'
    TIPOC54	= 'POR DISBARISMO'
    TIPOC55	= 'POR HIPERVENTILAÇÃO'
    TIPOC56	= 'POR HIPÓXIA'
    TIPOC57	= 'POR PROBLEMAS FISIOLÓGICOS'
    TIPOC58	= 'POR PROBLEMAS PSICOLÓGICOS'
    TIPOC59	= 'POUSO ANTES DA PISTA'
    TIPOC60	= 'POUSO BRUSCO'
    TIPOC61	= 'POUSO DE EMERGÊNCIA'
    TIPOC62	= 'POUSO DE PRECAUÇÃO'
    TIPOC63	= 'POUSO EM LOCAL NÃO PREVISTO'
    TIPOC64	= 'POUSO FORÇADO/ABANDONO DA AERONAVE EM VOO'
    TIPOC65	= 'POUSO LONGO'
    TIPOC66	= 'POUSO SEM TREM'
    TIPOC67	= 'SAÍDA DE PISTA'
    TIPOC68	= 'SOPRO DE HÉLICE'
    TIPOC69	= 'SOPRO DE REATOR'
    TIPOC70	= 'SOPRO DE ROTOR'
    TIPOC71	= 'SUPERAQUECIMENTO'
    TIPOC72	= 'TRÁFEGO AÉREO'
    TIPOC73	= 'VAZAMENTO DE COMBUSTÍVEL'
    TIPOC74	= 'VAZAMENTO DE OUTROS FLUÍDOS'
    TIPOCORRENCIA = (
        (	TIPOC1	, 'AERONAVE ATINGIDA POR OBJETO'),
        (	TIPOC2	, 'ALARME FALSO OU SUPERAQUECIMENTO'),
        (	TIPOC3	, 'CAUSADO POR FENOMENO METEOROLÓGICO EM VOO'),
        (	TIPOC4	, 'CAUSADO POR FENOMENO METEOROLÓGICO NO SOLO'),
        (	TIPOC5	, 'CAUSADO POR RICOCHETE'),
        (	TIPOC6	, 'CFIT'),
        (	TIPOC7	, 'COLISÃO COM AERONAVE NO SOLO'),
        (	TIPOC8	, 'COLISÃO COM OBSTÁCULO NO SOLO'),
        (	TIPOC9	, 'COLISÃO COM PÁSSARO'),
        (	TIPOC10	, 'COLISÃO DE AERONAVES EM VOO'),
        (	TIPOC11	, 'COLISÃO DE VEÍCULO COM AERONAVE'),
        (	TIPOC12	, 'COLISÃO EM VOO COM OBJETO REBOCADO'),
        (	TIPOC13	, 'COM CANOPI'),
        (	TIPOC14	, 'COM COMANDOS DE VOO'),
        (	TIPOC15	, 'COM HÉLICE'),
        (	TIPOC16	, 'COM LANÇAMENTO OU TRANSPORTE DE CARGA'),
        (	TIPOC17	, 'COM LANÇAMENTO OU TRANSPORTE DE PESSOAS'),
        (	TIPOC18	, 'COM PÁRA-BRISAS/JANELA/PORTA'),
        (	TIPOC19	, 'COM PESSOAL EM VOO'),
        (	TIPOC20	, 'COM ROTOR'),
        (	TIPOC21	, 'COM TREM DE POUSO'),
        (	TIPOC22	, 'COM TURBINA'),
        (	TIPOC23	, 'CORTE INVOLUNTÁRIO DO MOTOR'),
        (	TIPOC24	, 'DE TRÁFEGO AÉREO'),
        (	TIPOC25	, 'DESCOMPRESSÃO NÃO INTENCIONAL / EXPLOSIVA'),
        (	TIPOC26	, 'DESORIENTAÇÃO ESPACIAL / ATITUDE ANORMAL'),
        (	TIPOC27	, 'DISPARO INVOLUNTÁRIO DE ARMAMENTO'),
        (	TIPOC28	, 'EJEÇÃO INVOLUNTÁRIA'),
        (	TIPOC29	, 'ESTOURO DE PNEU'),
        (	TIPOC30	, 'EXCURSÃO DE PISTA'),
        (	TIPOC31	, 'EXPLOSÃO'),
        (	TIPOC32	, 'EXPOSIÇÃO A SUBSTÂNCIA TÓXICA'),
        (	TIPOC33	, 'F.O.D.'),
        (	TIPOC34	, 'FALHA DE SISTEMA / COMPONENTE'),
        (	TIPOC35	, 'FALHA DO MOTOR EM VOO'),
        (	TIPOC36	, 'FALHA DO MOTOR NO SOLO'),
        (	TIPOC37	, 'FALHA ESTRUTURAL'),
        (	TIPOC38	, 'FOGO EM VOO'),
        (	TIPOC39	, 'FOGO NO SOLO'),
        (	TIPOC40	, 'FUMAÇA'),
        (	TIPOC41	, 'FUMAÇA NA CABINE'),
        (	TIPOC42	, 'INCIDENTE C/ HÉLICE/ ROTOR / TURBINA'),
        (	TIPOC43	, 'INCURSÃO EM PISTA'),
        (	TIPOC44	, 'INDETERMINADA'),
        (	TIPOC45	, 'INDICAÇÃO FALSA DE INSTRUMENTO'),
        (	TIPOC46	, 'MANOBRAS A BAIXA ALTURA'),
        (	TIPOC47	, 'OUTROS TIPOS'),
        (	TIPOC48	, 'PANE SECA'),
        (	TIPOC49	, 'PERDA DA CONSCIÊNCIA'),
        (	TIPOC50	, 'PERDA DE COMPONENTE EM VOO'),
        (	TIPOC51	, 'PERDA DE COMPONENTE NO SOLO'),
        (	TIPOC52	, 'PERDA DE CONTROLE EM VOO'),
        (	TIPOC53	, 'PERDA DE CONTROLE NO SOLO'),
        (	TIPOC54	, 'POR DISBARISMO'),
        (	TIPOC55	, 'POR HIPERVENTILAÇÃO'),
        (	TIPOC56	, 'POR HIPÓXIA'),
        (	TIPOC57	, 'POR PROBLEMAS FISIOLÓGICOS'),
        (	TIPOC58	, 'POR PROBLEMAS PSICOLÓGICOS'),
        (	TIPOC59	, 'POUSO ANTES DA PISTA'),
        (	TIPOC60	, 'POUSO BRUSCO'),
        (	TIPOC61	, 'POUSO DE EMERGÊNCIA'),
        (	TIPOC62	, 'POUSO DE PRECAUÇÃO'),
        (	TIPOC63	, 'POUSO EM LOCAL NÃO PREVISTO'),
        (	TIPOC64	, 'POUSO FORÇADO/ABANDONO DA AERONAVE EM VOO'),
        (	TIPOC65	, 'POUSO LONGO'),
        (	TIPOC66	, 'POUSO SEM TREM'),
        (	TIPOC67	, 'SAÍDA DE PISTA'),
        (	TIPOC68	, 'SOPRO DE HÉLICE'),
        (	TIPOC69	, 'SOPRO DE REATOR'),
        (	TIPOC70	, 'SOPRO DE ROTOR'),
        (	TIPOC71	, 'SUPERAQUECIMENTO'),
        (	TIPOC72	, 'TRÁFEGO AÉREO'),
        (	TIPOC73	, 'VAZAMENTO DE COMBUSTÍVEL'),
        (	TIPOC74	, 'VAZAMENTO DE OUTROS FLUÍDOS')
    )

############################################
#FATOR TAXONOMIA
############################################
class FatorTaxonomia():
    #AREA
    OUTRO = '***'
    HUMANO = 'HUMANO'
    MATERIAL = 'MATERIAL'
    OPERACIONAL = 'OPERACIONAL'
    AREA = (
        (OUTRO, '***'),
        (HUMANO, 'HUMANO'),
        (MATERIAL, 'MATERIAL'),
        (OPERACIONAL, 'OPERACIONAL')
    )

    #ASPECTO
    OUTRO = '***'
    MATERIAL = 'MATERIAL'
    MEDICO = 'MÉDICO'
    OPERACIONAL = 'OPERACIONAL'
    PSICOLOGICO = 'PSICOLÓGICO'
    ASPECTO = (
        (OUTRO, '***'),
        (MATERIAL, 'MATERIAL'),
        (MEDICO, 'MÉDICO'),
        (OPERACIONAL, 'OPERACIONAL'),
        (PSICOLOGICO, 'PSICOLÓGICO')
    )

    #CONDICIONANTE
    OUTRO = '***'
    INDIVIDUAL = 'INDIVIDUAL'
    ORGANIZACIONAL = 'ORGANIZACIONAL'
    PSICOSOCIAL = 'PSICOSOCIAL'
    CONDICIONANTE = (
        (OUTRO, '***'),
        (INDIVIDUAL, 'INDIVIDUAL'),
        (ORGANIZACIONAL, 'ORGANIZACIONAL'),
        (PSICOSOCIAL, 'PSICOSOCIAL')
    )

############################################
#FATORCOCORRENCIA TAXONOMIA
############################################
class FatorOcorrenciaTaxonomia():
    #NIVEL CONTRIBUICAO
    OUTRO = '***'
    CONTRIBUIU = 'CONTRIBUIU'
    INDETERMINADO = 'INDETERMINADO'
    LATENTE = 'LATENTE'
    NIVELCONTRIBUICAO = (
        (OUTRO, '***'),
        (CONTRIBUIU, 'CONTRIBUIU'),
        (INDETERMINADO, 'INDETERMINADO'),
        (LATENTE, 'LATENTE')
    )

    #RELATORIO
    OUTRO = '***'
    RP = 'RP'
    RF = 'RF'
    SUMA = 'SUMA'
    RELATORIO = (
        (OUTRO, '***'),
        (RP, 'RELATÓRIO PRELIMINAR'),
        (RF, 'RELATÓRIO FINAL'),
        (SUMA, 'SUMA')
    )

############################################
#AERONAVECATEGORIA TAXONOMIA
############################################
class AeronaveCategoriaTaxonomia():
    #REGULAMENTO
    REG1 = '***'
    REG2 = 'RBHA 91'
    REG3 = 'RBHA 91/140'
    REG4 = 'RBAC 137'
    REG5 = 'RBAC 121'
    REG6 = 'RBAC 135'
    REG7 = 'RBAC 135/RBHA 91'
    REGULAMENTO = (
        (REG1, '***'),
        (REG2, 'RBHA 91'),
        (REG3, 'RBHA 91/140'),
        (REG4, 'RBAC 137'),
        (REG5, 'RBAC 121'),
        (REG6, 'RBAC 135'),
        (REG7, 'RBAC 135/RBHA 91')
    )

    #AVIACAO
    AVI1 = '***'
    AVI2 = 'GERAL'
    AVI3 = 'INSTRUÇÃO'
    AVI4 = 'AGRÍCOLA'
    AVI5 = 'REGULAR'
    AVI6 = 'TÁXI AÉREO'
    AVI7 = 'MÚLTIPLA'
    AVI8 = 'EXPERIMENTAL'
    AVIACAO = (
        (AVI1, '***'),
        (AVI2, 'GERAL'),
        (AVI3, 'INSTRUÇÃO'),
        (AVI4, 'AGRÍCOLA'),
        (AVI5, 'REGULAR'),
        (AVI6, 'TÁXI AÉREO'),
        (AVI7, 'MÚLTIPLA'),
        (AVI8, 'EXPERIMENTAL')
    )

############################################
#AERONAVE TAXONOMIA
############################################
class AeronaveTaxonomia():
    #CLASSIFICACAO DA AERONAVE
    CIVIL = 'CIVIL'
    MILITAR = 'MILITAR'
    OUTRA = '***'
    CLASSIFICACAO = (
        (OUTRA, '***'),
        (CIVIL, 'CIVIL'),
        (MILITAR, 'MILITAR')
    )

    #TREM DE POUSO
    TREMP1 = 'CONVENCIONAL'
    TREMP2 = 'ESCAMOTEÁVEL'
    TREMP3 = 'FIXO'
    TREMP4 = 'POUSO NA ÁGUA'
    TREMP5 = 'TRICICLO'
    TREMP6 = 'TRICICLO FIXO'
    TREMP7 = 'TRICICLO RETRÁTIL'
    TREMP8 = '***'
    TIPOTREMPOUSO = (
        (TREMP1 , 'CONVENCIONAL'),
        (TREMP2 , 'ESCAMOTEÁVEL'),
        (TREMP3 , 'FIXO'),
        (TREMP4 , 'POUSO NA ÁGUA'),
        (TREMP5 , 'TRICICLO'),
        (TREMP6 , 'TRICICLO FIXO'),
        (TREMP7 , 'TRICICLO RETRÁTIL'),
        (TREMP8 , '***')
    )

    #TIPO DE MOTOR
    TIPOM1 = 'CONVENCIONAL'
    TIPOM2 = 'JATO'
    TIPOM3 = 'TURBOÉLICE'
    TIPOM4 = 'TURBOEIXO'
    TIPOM5 = 'SEM TRAÇÃO'
    TIPOM6 = '***'
    TIPOMOTOR = (
        (TIPOM1 , 'CONVENCIONAL'),
        (TIPOM2 , 'JATO'),
        (TIPOM3 , 'TURBOÉLICE'),
        (TIPOM4 , 'TURBOEIXO'),
        (TIPOM5 , 'SEM TRAÇÃO'),
        (TIPOM6 , '***')
    )

    #EQUIPAMENTO
    EQUIP1 = 'AVIÃO'
    EQUIP2 = 'ANFÍBIO'
    EQUIP3 = 'BALÃO'
    EQUIP4 = 'DIRIGÍVEL'
    EQUIP5 = 'GIROCÓPTERO'
    EQUIP6 = 'HELICÓPTERO'
    EQUIP7 = 'PLANADOR'
    EQUIP8 = 'ULTRALEVE'
    EQUIP9 = 'MOTOPLANADOR'
    EQUIP10 = 'EXPERIMENTAL'
    EQUIP11 = 'TRIKE'
    EQUIP12 = 'PROTÓTIPO'
    EQUIP13 = 'VANT'
    EQUIP14 = 'PARAGLIDER'
    EQUIP15 = '***'
    EQUIPAMENTO = (
        (EQUIP1 , 'AVIÃO'),
        (EQUIP2 , 'ANFÍBIO'),
        (EQUIP3 , 'BALÃO'),
        (EQUIP4 , 'DIRIGÍVEL'),
        (EQUIP5 , 'GIROCÓPTERO'),
        (EQUIP6 , 'HELICÓPTERO'),
        (EQUIP7 , 'PLANADOR'),
        (EQUIP8 , 'ULTRALEVE'),
        (EQUIP9 , 'MOTOPLANADOR'),
        (EQUIP10 , 'EXPERIMENTAL'),
        (EQUIP11 , 'TRIKE'),
        (EQUIP12 , 'PROTÓTIPO'),
        (EQUIP13 , 'VANT'),
        (EQUIP14 , 'PARAGLIDER'),
        (EQUIP15 , '***')
    )

    #CLASSE
    CLAS1 = '***'
    CLAS2 = 'A1P'
    CLAS3 = 'A1T'
    CLAS4 = 'A2P'
    CLAS5 = 'A4P'
    CLAS6 = 'G1P'
    CLAS7 = 'H1P'
    CLAS8 = 'H1T'
    CLAS9 = 'H2T'
    CLAS10 = 'L00'
    CLAS11 = 'L1J'
    CLAS12 = 'L1P'
    CLAS13 = 'L1T'
    CLAS14 = 'L2J'
    CLAS15 = 'L2P'
    CLAS16 = 'L2T'
    CLAS17 = 'L3J'
    CLAS18 = 'L4J'
    CLAS19 = 'L4P'
    CLAS20 = 'L4T'
    CLAS21 = 'S1P'
    CLASSE = (
        (CLAS1, '***'),
        (CLAS2, 'A1P'),
        (CLAS3, 'A1T'),
        (CLAS4, 'A2P'),
        (CLAS5, 'A4P'),
        (CLAS6, 'G1P'),
        (CLAS7, 'H1P'),
        (CLAS8, 'H1T'),
        (CLAS9, 'H2T'),
        (CLAS10, 'L00'),
        (CLAS11, 'L1J'),
        (CLAS12, 'L1P'),
        (CLAS13, 'L1T'),
        (CLAS14, 'L2J'),
        (CLAS15, 'L2P'),
        (CLAS16, 'L2T'),
        (CLAS17, 'L3J'),
        (CLAS18, 'L4J'),
        (CLAS19, 'L4P'),
        (CLAS20, 'L4T'),
        (CLAS21, 'S1P')
    )

############################################
#AERONAVEOCORRENCIA TAXONOMIA
############################################
class AeronaveOcorrenciaTaxonomia():
    #DANOS DA AERONAVE
    NENHUM = 'NENHUM'
    LEVE = 'LEVE'
    GRAVE = 'GRAVE'
    TOTAL = 'TOTAL'
    DANOS = (
        (NENHUM, 'NENHUM'),
        (LEVE, 'LEVE'),
        (GRAVE, 'GRAVE'),
        (TOTAL, 'TOTAL')
    )

    #OPERACAO
    OP1 = 'AGRÍCOLA'
    OP2 = 'ESPECIALIZADA'
    OP3 = 'EXPERIMENTAL'
    OP4 = 'INSTRUÇÃO'
    OP5 = 'POLICIAL'
    OP6 = 'PRIVADA'
    OP7 = 'PÚBLICA'
    OP8 = 'SAE'
    OP9 = 'TÁXI AÉREO'
    OP10 = 'REGULAR'
    OP11 = 'NÃO REGULAR'
    OP12 = '***'
    OPERACAO =(
        (OP1, 'AGRÍCOLA'),
        (OP2, 'ESPECIALIZADA'),
        (OP3, 'EXPERIMENTAL'),
        (OP4, 'INSTRUÇÃO'),
        (OP5, 'POLICIAL'),
        (OP6, 'PRIVADA'),
        (OP7, 'PÚBLICA'),
        (OP8, 'SAE'),
        (OP9, 'TÁXI AÉREO'),
        (OP10, 'REGULAR'),
        (OP11, 'NÃO REGULAR'),
        (OP12, '***'),
    )

############################################
#LESOES TAXONOMIA
############################################
class LesoesTaxonomia():
    #TIPO LESAO
    TIPO1 = 'DESCONHECIDO'
    TIPO2 = 'LEVE'
    TIPO3 = 'ILESO'
    TIPO4 = 'GRAVE'
    TIPO5 = 'FATAL'
    TIPO = (
        (TIPO1 , 'DESCONHECIDO'),
        (TIPO2 , 'LEVE'),
        (TIPO3 , 'ILESO'),
        (TIPO4 , 'GRAVE'),
        (TIPO5 , 'FATAL')
    )

    #PESSOA LESAO
    PESSOA1 = 'PASSAGEIRO'
    PESSOA2 = 'TRIPULANTE'
    PESSOA3 = 'TERCEIROS'
    PESSOA =(
        (PESSOA1 , 'PASSAGEIRO'),
        (PESSOA2 , 'TRIPULANTE'),
        (PESSOA3 , 'TERCEIROS')
    )

































'''

############################################
#DOCUMENTO
############################################
class DocumentoTaxonomia():
    #TIPO DO DOCUMENTO
    FNCO = 'FNCO'
    RAI = 'RAI'
    RP = 'RP'
    RF = 'RF'
    SUMA = 'SUMA'
    OFICIO = 'OFICIO'
    RADIO = 'RADIO'
    TIPO = (
        (OFICIO, 'OFICIO'),
        (FNCO, 'FNCO'),
        (RAI, 'RAI'),
        (RP, 'RP'),
        (RF, 'RF'),
        (SUMA, 'SUMA'),
	(RADIO, 'RADIO')
    )

    #STATUS DOCUMENTO
    AUTENTICADO = 'AUTENTICADO'
    RECUSADO = 'RECUSADO'
    PUBLICADO = 'PUBLICADO'
    SITUACAO = (
        (AUTENTICADO, 'AUTENTICADO'),
        (RECUSADO, 'RECUSADO'),
        (PUBLICADO, 'PUBLICADO')
    )

    #DESPACHO
    RECEBIDO = 'RECEBIDO'
    ENVIADO = 'ENVIADO'
    OUTRO = '***'
    DESPACHO = (
        (RECEBIDO, 'RECEBIDO'),
        (ENVIADO, 'ENVIADO'),
        (OUTRO, '***')
    )

############################################
#TRIPULACAO TAXONOMIA
############################################
class TripulacaoTaxonomia():
    #FUNCAO A BORDO
    FUNCAO1 = 'PILOTO'
    FUNCAO2 = 'CO-PILOTO'
    FUNCAO3 = 'ALUNO'
    FUNCAO4 = 'INSTRUTOR'
    FUNCAO5 = 'CHECADOR'
    FUNCAO6 = 'MECÂNICO'
    FUNCAO7 = 'EXAMINADOR'
    FUNCAOTRIPULANTE = (
        (FUNCAO1 , 'PILOTO'),
        (FUNCAO2 , 'CO-PILOTO'),
        (FUNCAO3 , 'ALUNO'),
        (FUNCAO4 , 'INSTRUTOR'),
        (FUNCAO5 , 'CHECADOR'),
        (FUNCAO6 , 'MECÂNICO'),
        (FUNCAO7 , 'EXAMINADOR')
    )

############################################
#RECOMENDACOES TAXONOMIA
############################################
class RecomendacaoSegurancaTaxonomia():
    #APLICACAO
    APLIC1 = 'REGULAMENTAÇÃO'
    APLIC2 = 'FISCALIZAÇÃO'
    APLIC3 = 'NOTIFICAÇÃO'
    APLIC4 = 'DIVULGAÇÃO'
    APLIC5 = 'TREINAMENTO'
    APLIC6 = 'TECNOLOGIA'
    APLIC7 = 'ADMINISTRATIVA'
    APLIC8 = 'OUTRA APLICAÇÃO'
    APLICACAO = (
        (APLIC1 , 'REGULAMENTAÇÃO'),
        (APLIC2 , 'FISCALIZAÇÃO'),
        (APLIC3 , 'NOTIFICAÇÃO'),
        (APLIC4 , 'DIVULGAÇÃO'),
        (APLIC5 , 'TREINAMENTO'),
        (APLIC6 , 'TECNOLOGIA'),
        (APLIC7 , 'ADMINISTRATIVA'),
        (APLIC8 , 'OUTRA APLICAÇÃO')
    )
    #SITUACAO
    SITU1 = 'AGUARDANDO RESPOSTA'
    SITU2 = 'NÃO CUMPRIDA'
    SITU3 = 'CUMPRIDA PARCIALMENTE'
    SITU4 = 'CUMPRIDA'
    SITUACAO = (
        (SITU1 , 'AGUARDANDO RESPOSTA'),
        (SITU2 , 'NÃO CUMPRIDA'),
        (SITU3 , 'CUMPRIDA PARCIALMENTE'),
        (SITU4 , 'CUMPRIDA')
    )

############################################
#CONTROLE INVESTIGAÇÃO
############################################
class InvestigacaoTaxonomia():
    #FASE DA INVESTIGAÇÃO
    FNCO = 'FNCO'
    RAI = 'RAI'
    RP = 'RP'
    RF = 'RF'
    SUMA = 'SUMA'
    ULTIMAFASE = (
        (FNCO, 'FNCO'),
        (RAI, 'RAI'),
        (RP, 'RP'),
        (RF, 'RF'),
        (SUMA, 'SUMA')
    )

    #COMANDO INVESTIGADOR
    SERIPA1 = 'SERIPA-1'
    SERIPA2 = 'SERIPA-2'
    SERIPA3 = 'SERIPA-3'
    SERIPA4 = 'SERIPA-4'
    SERIPA5 = 'SERIPA-5'
    SERIPA6 = 'SERIPA-6'
    SERIPA7 = 'SERIPA-7'
    CENIPA = 'CENIPA'
    OPERADOR_A = 'OPERADOR AÉREO'
    OPERADOR_B = 'OPERADOR AEROPORTUÁRIO'
    COMANDOINVESTIGADOR = (
        (SERIPA1, 'SERIPA-1'),
        (SERIPA2, 'SERIPA-2'),
        (SERIPA3, 'SERIPA-3'),
        (SERIPA4, 'SERIPA-4'),
        (SERIPA5, 'SERIPA-5'),
        (SERIPA6, 'SERIPA-6'),
        (SERIPA7, 'SERIPA-7'),
        (CENIPA, 'CENIPA'),
        (OPERADOR_A, 'OPERADOR AÉREO'),
        (OPERADOR_B, 'OPERADOR AEROPORTUÁRIO')
    )

    # SITUACAO OCORRENCIA
    NAO_INVESTIGADO = 'NÃO INVESTIGADO'
    INVESTIGADO = 'INVESTIGADO'
    DECISAO = (
        (NAO_INVESTIGADO, 'NÃO INVESTIGADO'),
        (INVESTIGADO, 'INVESTIGADO')
    )

    #STATUS SITUACAO
    ATIVA = 'ATIVA'
    FINALIZADA = 'FINALIZADA'
    SITUACAO = (
        (ATIVA, 'ATIVA'),
        (FINALIZADA, 'FINALIZADA')
    )

'''



