
#CLASSIFICACAO
class ClassificacaoTaxonomia():
    ACIDENTE = 'ACIDENTE'
    INCIDENTE_GRAVE = 'INCIDENTE GRAVE'
    INCIDENTE = 'INCIDENTE'
    ANORMAL = 'ANORMAL'
    CLASSIFICACAO = ((ACIDENTE, 'ACIDENTE'),
                    (INCIDENTE_GRAVE, 'INCIDENTE GRAVE'),
                    (INCIDENTE, 'INCIDENTE'),
                    (ANORMAL, 'ANORMAL'))
    def __str__(self):
        return self.CLASSIFICACAO

#COMANDO INVESTIGADOR
class ComandoTaxonomia():
    SERIPA1 = 'SERIPA-1'
    SERIPA2 = 'SERIPA-2'
    SERIPA3 = 'SERIPA-3'
    SERIPA4 = 'SERIPA-4'
    SERIPA5 = 'SERIPA-5'
    SERIPA6 = 'SERIPA-6'
    SERIPA7 = 'SERIPA-7'
    CENIPA = 'CENIPA'
    OPERADOR = 'OPERADOR'
    COMANDO = (
        (SERIPA1, 'SERIPA-1'),
        (SERIPA2, 'SERIPA-2'),
        (SERIPA3, 'SERIPA-3'),
        (SERIPA4, 'SERIPA-4'),
        (SERIPA5, 'SERIPA-5'),
        (SERIPA6, 'SERIPA-6'),
        (SERIPA7, 'SERIPA-7'),
        (CENIPA, 'CENIPA'),
        (OPERADOR, 'OPERADOR')
    )
    def __str__(self):
        return self.COMANDO

#DANOS DA AERONAVE

class AeronaveTaxonomia():
    NENHUM = 'NENHUM'
    LEVE = 'LEVE'
    GRAVE = 'GRAVE'
    TOTAL = 'TOTAL'
    DANOS = ((NENHUM, 'NENHUM'),
            (LEVE, 'LEVE'),
            (GRAVE, 'GRAVE'),
            (TOTAL, 'TOTAL'))
    def __str__(self):
        return self.DANOS


#CONTRIBUICAO DO FATOR
class FatorContribuicao():
    CONTRIBUIU = 'CONTRIBUIU'
    INDETERMINADO = 'INDETERMINADO'
    NAO_CONTRIBUIU = 'NAO CONTRIBUIU'
    TAXONOMIA = (
            (CONTRIBUIU, 'CONTRIBUIU'),
            (INDETERMINADO, 'INDETERMINADO'),
            (NAO_CONTRIBUIU, 'NAO CONTRIBUIU'))
    def __str__(self):
        return self.TAXONOMIA
		
#INSERIR TODOS