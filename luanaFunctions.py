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
    return [gera_lista_robo_alvo(ID_robo_alvo, lista_geral)]




def organiza_saida(ID_robo_alvo, lista_geral, dist):
    if lista_geral = []: return []
    else: return (get_ID(lista_geral), dist, [get_Locate(lista_geral[0])] + organiza_saida(ID_robo_alvo, lista_geral[1:], dist))

'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que ordena
INPUTS: Id do robo e a lista geral
OUTPUT: A lista das distâncias ordenadas
'''
def jordana_sort(lista):
    def ajuda_jordana(lista1, lista2):
        if not lista1: return lista2
        elif not lista2: return lista1
        elif lista1[0] <= lista2[0]: return [lista1[0]] + ajuda_jordana(lista1[1:], lista2)
        else: return [lista2[0]] + ajuda_jordana(lista1, lista2[1:])

    if len(lista) <= 1: return lista
    else: return ajuda_jordana(jordana_sort(lista[:len(lista)//2]),jordana_sort(lista[len(lista)//2:]))


# id = lista[0][0]
lista_aa = [('robo3', 1, (7, 7), 3), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo3', 8, (7, 2), 3)]
lista_teste = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]
# print(retorna_dist_pontos('robo3', lista_teste))









'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que retorna todos os pontos de um robo especifico
INPUTS: Lista com as informacoes de um robo especifico
OUTPUT: A distancia e uma lista com todas as ocorrencias do robo
'''

def get_all_Locates(lista):
    if lista == []: return []
    else: return [get_Locate(lista)] + get_all_Locates(lista[1:])

'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que retorna organiza o formato de saida de um robo
INPUTS: Id do robo e a lista geral
OUTPUT: Id do robo, a distancia e a lista de pontos
'''
def organiza_inf_ID(ID_robo_alvo, lista_geral):
    dist = distPercorridaRobo(ID_robo_alvo, lista_geral)
    lista_pontos = get_all_Locates(gera_lista_robo_alvo(ID_robo_alvo, lista_geral))
    return (ID_robo_alvo, dist, lista_pontos)

'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que retorna organiza o formato de saida geral
INPUTS: Lista de IDs e a lista geral
OUTPUT: Id do robo, a distancia e a lista de pontos de cada robo
'''
def inf_All_IDs(lista_IDs, lista_geral):
    if lista_IDs == []: return []
    else: return [organiza_inf_ID(lista_IDs[0], lista_geral)] + inf_All_IDs(lista_IDs[1:], lista_geral)
    

'''
FUNCAO AUXILIAR PARAMETRICA DE QUESTAO 'C':
OBJETIVO: Funcao que ordena
INPUTS: Id do robo e a lista geral
OUTPUT: A lista das distâncias ordenadas
'''
def jordana_sort(lista):
    def ajuda_jordana(lista1, lista2):
        if not lista1: return lista2
        elif not lista2: return lista1
        elif second_list(lista1[0]) <= second_list(lista2[0]): return [lista1[0]] + ajuda_jordana(lista1[1:], lista2)
        else: return [lista2[0]] + ajuda_jordana(lista1, lista2[1:])

    if len(lista) <= 1: return lista
    else: return ajuda_jordana(jordana_sort(lista[:len(lista)//2]),jordana_sort(lista[len(lista)//2:]))

'''
FUNCAO PRINCIPAL DA QUESTAO A:
OBJETIVO: Ordena de forma crescente os robos e printa os pontos
INPUTS: Uma lista geral
OUTPUT: Retorna uma lista de tuplas em ordem crescente pelo ID.
'''
def aa(lista_geral):
    lista_IDs = retira_repetidos(gera_lista_robo(lista_geral))
    return inf_All_IDs(lista_IDs, lista_geral)