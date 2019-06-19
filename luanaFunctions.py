# c) Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca, ordenados crescentemente pela distância total percorrida

'''
[(id, instanteAreaAfetada, ponto, vitimasNaVisibilidade)...]
'''

'''
Letra C
Exiba os caminhos percorridos por todos os robôs que entraram no terreno de busca, 
ordenados crescentemente pela distância total percorrida;


Preciso de:
    distancia de todos os robos com o id
        lista com todos os ids & lista completa
        retira repetidos da lista com ids
        funcao recursiva
'''
'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que retorna a distancia e as informacoes de um robo especifico
INPUTS: Id do robo e a lista geral
OUTPUT: A distancia e uma lista com todas as ocorrencias do robo
'''
def retorna_dist_pontos(ID_robo_alvo, lista_geral):
    dist = distPercorridaRobo(ID_robo_alvo, lista_geral)
    return [dist, gera_lista_robo_alvo(ID_robo_alvo, lista_geral)]

def ordena_dist(ID_robo_alvo, lista_geral):
    if lista_geral == []: return []
    else if
