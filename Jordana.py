'''
* * * * * * * * * * * * * * * * * * * * *
* NOME:                                 *
*     > EZEQUIEL SCHNEIDER REINHOLTZ    *
*     > LUANA GABRIELE DE SOUSA COSTA   *
*                                       *
* PROFESSORA:                           *
*     > JORDANA SARMENGHI SALAMON       *
*                                       *
* MATERIA:                              *
*     > PROGRAMACAO 1                   *
*                                       *
* CURSO:                                *
*     > CIÊNCIA DA COMPUTAÇÃO - 2019/1  *
*                                       *
* TRABALHO:                             *
*     > ROBOZIN DO SAMU                 *
*                                       *
* * * * * * * * * * * * * * * * * * * * *
'''

'''IMPORTACAO DE FUNCOES'''
from math import sqrt
from functools import reduce


'''FUNCOES FULL GLOBAIS'''

'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o ID do robo do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID_1', Time, (P1, P2), People), ('ID_2', ...), ... , ('ID_n', ...)]
OUTPUT: Retorna o ID do robo referente a primeira tupla de uma lista
'''
def get_ID(lista):
    return lista[0][0]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o Tempo do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., Time_2, ...), ... , (..., Time_n, ...)]
OUTPUT: Retorna o Tempo referente a primeira tupla de uma lista
'''
def get_Time(lista):
    return lista[0][1]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o Local de acidente do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., (X1, X2), ...), ... , (..., (Y1, Y2), ...)]
OUTPUT: Retorna o Local do acidente referente a primeira tupla de uma lista
'''
def get_Locate(lista):
    return lista[0][2]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o numero de pessoas avistadas do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., People), ... , (..., People)]
OUTPUT: Retorna o numero de pessoas avisatadas referente a primeira tupla de uma lista
'''
def get_People(lista):
    return lista[0][3]



'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que retorna o tamanho da lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o tamanho da lista de entrada
'''
def tamanho_list(lista):
    return len(lista)


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o primeiro elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o primeiro elemento de uma lista
'''
def first_list(lista):
    return lista[0]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o ultimo elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o ultimo elemento de uma lista
'''
def last_list(lista):
    return lista[-1]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o segundo elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o segundo elemento de uma lista
'''
def second_list(lista):
    return lista[0]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna todos os elementos menos o primeiro de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna todos os elementos menos o primeiro de uma lista
'''
def rest_list(lista):
    return lista[1:]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna todos os elementos menos o ultimo de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna todos os elementos menos o ultimo de uma lista
'''
def begin_list(lista):
    return lista[:-1]


'''
FUNCAO AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que verifica se a lista de entrada esta vazia
INPUTS: Uma lista 'lista'
OUTPUT: Retorna 'True' se a lista for vazia e 'False' caso contrario
'''
def lista_vazia(lista):
    if lista == []:
        return True
    else:
        return False


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com as informacoes do ID do robo dado como entrada
INPUTS: Uma string 'ID_robo_alvo' para robo alvo da lista, Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com todas as informacoes do robo alvo
'''
def gera_lista_robo_alvo(ID_robo_alvo, lista_geral):
        if lista_vazia(lista_geral):
            return lista_geral
        elif get_ID(lista_geral) == ID_robo_alvo:
            return [first_list(lista_geral)] + gera_lista_robo_alvo(ID_robo_alvo, rest_list(lista_geral))
        else:
            return gera_lista_robo_alvo(ID_robo_alvo, rest_list(lista_geral))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com os Tempos do(os) robo(os) da lista de entrada
INPUTS: Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com os Tempos do(os) robo(os)
'''
def gera_lista_robo(lista_alvo):
        if lista_vazia(lista_alvo):
            return lista_alvo
        else:
            return [get_ID(lista_alvo)] + gera_lista_robo(rest_list(lista_alvo))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com os Tempos do(os) robo(os) da lista de entrada
INPUTS: Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com os Tempos do(os) robo(os)
'''
def gera_lista_Time(lista_alvo):
        if lista_vazia(lista_alvo):
            return lista_alvo
        else:
            return [get_Time(lista_alvo)] + gera_lista_Time(rest_list(lista_alvo))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com os locais acidentados do(os) robo(os) da lista de entrada
INPUTS: Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com os locais acidentados do(os) robo(os)
'''
def gera_lista_Locate(lista_alvo):
        if lista_vazia(lista_alvo):
            return lista_alvo
        else:
            return [get_Locate(lista_alvo)] + gera_lista_Locate(rest_list(lista_alvo))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com as pessoas avistadas do(os) robo(os) da lista de entrada
INPUTS: Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com as pessoas avistadas do(os) robo(os)
'''
def gera_lista_People(lista_alvo):
        if lista_vazia(lista_alvo):
            return lista_alvo
        else:
            return [get_Peopĺe(lista_alvo)] + gera_lista_People(rest_list(lista_alvo))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'B':
OBJETIVO: Funcao que gera uma lista sem elementos repetidos da lista de entrada
INPUTS: Uma Lista 'lista' com elementos a serem avaliados
OUTPUT: Retorna uma lista sem os elementos repetidos
'''
def retira_repetidos(lista):
    if tamanho_list(lista) == 0:
        return []
    elif first_list(lista) in rest_list(lista):
        return retira_repetidos(rest_list(lista))
    else:
        return [first_list(lista)] + retira_repetidos(rest_list(lista))


'''==============================================================================================================''
* * * * * *
* PARTE A *
* * * * * *
'''

'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que retorna a coordenada 'X' de um ponto
INPUTS: Uma Tupla 'p' para um ponto
OUTPUT: Retorna o primeiro elemento da Tupla
'''
def returnXpoint(p):
    return p[0]


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que retorna a coordenada 'Y' de um ponto
INPUTS: Uma Tupla 'p' para um ponto
OUTPUT: Retorna o segundo elemento da Tupla
'''
def returnYpoint(p):
    return p[1]


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que calcula e retorna a distancia entre dois pontos
INPUTS: Uma Tupla 'p1' para o primeiro ponto, Uma Tupla 'p2' para o segundo ponto
OUTPUT: Retorna a distancia entre os pontos de entrada
'''
def distPoint(p1, p2):
    return sqrt((returnXpoint(p1) - returnXpoint(p2)) ** 2 + (returnYpoint(p1) - returnYpoint(p2)) ** 2)


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que retorna o calculo das distancias entre os pontos da lista de entrada
INPUTS: Uma Tupla 'ponto' para o ponto da distancia, Uma lista 'lista' para a lista de pontos
OUTPUT: Retorna a distancia entre os pontos de entrada
'''
def distLista(ponto, lista):
    if lista == []:
        return 0
    else:
        return distPoint(ponto, first_list(lista)) + distLista(second_list(lista), rest_list(lista[1:]))


'''
FUNCAO PRINCIPAL DA QUESTAO A:
OBJETIVO: Calcula a distancia percorrida por um robo especifico
INPUTS: Uma Lista 'l' com as informacoes do robo
OUTPUT: Retorna a distancia percorrida
'''
def distPercorridaRobo(ID_robo_alvo, lista_geral):
    return distLista((0,0), gera_lista_Locate(gera_lista_robo_alvo(ID_robo_alvo, lista_geral)))

'''==============================================================================================================''
* * * * * *
* PARTE B *
* * * * * *
'''

'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'B':
OBJETIVO: Funcao calcula e retorna as distancias entre o ponto de origem e a ultima localizacao dos robos
INPUTS: lista de entrada geral e uma lista dos robos da lista geral
OUTPUT: As distancias da origem e do ultimo local de cada robo
'''
def dist_end(lista_geral, lista_robos):
    if lista_vazia(lista_robos):
        return []
    else:
        return [(first_list(lista_robos), distPoint((0,0), get_Locate([last_list(gera_lista_robo_alvo(first_list(lista_robos), lista_geral))])))] + dist_end(lista_geral, rest_list(lista_robos))


'''
FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'B':
OBJETIVO: Funcao que mostra o robo que percorreu a maior distancia
INPUTS: lista de entrada geral
OUTPUT: A distancia e o ID do robo "mais cansado"
'''
def robo_maior_dist(lista_geral):
    '''
    FUNCAO AUXILIAR PARAMETRICA DA QUESTAO 'B':
    OBJETIVO: Funcao que calcula e retorna a maior distancia junto com o robo correspondente
    INPUTS: lista com as distancias finais de cada robo e o robo correspondente
    OUTPUT: A distancia e o ID do robo
    ''' 
    def maior_dist(a, b):
        if a[1] > b[1]:
            return a
        else:
            return b
        
    lista_gerada = gera_lista_robo_alvo(first_list(reduce(maior_dist, dist_end(lista_geral, retira_repetidos(gera_lista_robo(lista_geral))))), lista_geral)
    return (get_ID(lista_gerada), gera_lista_Locate(lista_gerada), lista_gerada[-1][1])
'''==============================================================================================================''[ 'robo3', 'robo4', 'robo3', 'robo5', 'robo5', 'robo6']
* * * * * *
* PARTE C *
* * * * * *
'''




'''==============================================================================================================''
* * * * * *
* PARTE D *
* * * * * *
'''

# def ID_mais_vitimas():
#     return lista_IDs



'''TESTES'''
lista_teste = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]
lista_rob = retira_repetidos(gera_lista_robo(lista_teste))
print(lista_rob)
print(gera_lista_robo_alvo('robo3', lista_teste))
print(robo_maior_dist(lista_teste))
#print(last_list(lista_teste[:-1]))
#print(get_Locate([last_list(lista_teste)]))
#print(robo_maior_dist(lista_teste))

'''
[(id, instanteAreaAfetada, ponto, vitimasNaVisibilidade)...]


-> Um robô não pode estar em dois pontos no mesmo instante
    if (id1 == id2 and ponto1 != ponto2): intante1 tem que ser =! de instante2
'''