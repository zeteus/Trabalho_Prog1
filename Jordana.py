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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o ID do robo do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID_1', Time, (P1, P2), People), ('ID_2', ...), ... , ('ID_n', ...)]
OUTPUT: Retorna o ID do robo referente a primeira tupla de uma lista
'''
def get_ID(lista):
    return lista[0][0]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o Tempo do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., Time_2, ...), ... , (..., Time_n, ...)]
OUTPUT: Retorna o Tempo referente a primeira tupla de uma lista
'''
def get_Time(lista):
    return lista[0][1]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o Local de acidente do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., (X1, X2), ...), ... , (..., (Y1, Y2), ...)]
OUTPUT: Retorna o Local do acidente referente a primeira tupla de uma lista
'''
def get_Locate(lista):
    return lista[0][2]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o numero de pessoas avistadas do primeiro elemento de uma lista dada
INPUTS: Uma lista 'lista' do modelo [('ID', Time_1, (P1, P2), People), (..., People), ... , (..., People)]
OUTPUT: Retorna o numero de pessoas avisatadas referente a primeira tupla de uma lista
'''
def get_People(lista):
    return lista[0][3]



'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que retorna o tamanho da lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o tamanho da lista de entrada
'''
def tamanho_list(lista):
    return len(lista)


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o primeiro elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o primeiro elemento de uma lista
'''
def first_list(lista):
    return lista[0]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o ultimo elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o ultimo elemento de uma lista
'''
def last_list(lista):
    return lista[-1]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna o segundo elemento de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna o segundo elemento de uma lista
'''
def second_list(lista):
    return lista[1]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna todos os elementos menos o primeiro de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna todos os elementos menos o primeiro de uma lista
'''
def rest_list(lista):
    return lista[1:]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
OBJETIVO: Funcao que acessa e retorna todos os elementos menos o ultimo de uma lista
INPUTS: Uma lista 'lista'
OUTPUT: Retorna todos os elementos menos o ultimo de uma lista
'''
def begin_list(lista):
    return lista[:-1]


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE TODAS AS QUESTOES:
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
OBJETIVO: Funcao que gera uma lista somente com as pessoas avistadas do(os) robo(os) da lista de entrada
INPUTS: Uma Lista 'lista_geral' para as informacoes de entrada geral
OUTPUT: Retorna uma lista com as pessoas avistadas do(os) robo(os)
'''
def gera_lista_People(lista_alvo):
        if lista_vazia(lista_alvo):
            return lista_alvo
        else:
            return [get_People(lista_alvo)] + gera_lista_People(rest_list(lista_alvo))


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'B':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DAS FUNCOES 'distLista', 'distPercorrida' e 'dist_end':
OBJETIVO: Funcao que calcula e retorna a distancia entre dois pontos
INPUTS: Uma Tupla 'p1' para o primeiro ponto, Uma Tupla 'p2' para o segundo ponto
OUTPUT: Retorna a distancia entre os pontos de entrada
'''
def distPoint(p1, p2):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
    OBJETIVO: Funcao que retorna a coordenada 'X' de um ponto
    INPUTS: Uma Tupla 'p' para um ponto
    OUTPUT: Retorna o primeiro elemento da Tupla
    '''
    def returnXpoint(p):
        return p[0]

    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DA QUESTAO 'A':
    OBJETIVO: Funcao que retorna a coordenada 'Y' de um ponto
    INPUTS: Uma Tupla 'p' para um ponto
    OUTPUT: Retorna o segundo elemento da Tupla
    '''
    def returnYpoint(p):
        return p[1]

    return sqrt((returnXpoint(p1) - returnXpoint(p2)) ** 2 + (returnYpoint(p1) - returnYpoint(p2)) ** 2)


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA FUNCAO 'distPercorrida':
OBJETIVO: Funcao que retorna o calculo das distancias entre os pontos da lista de entrada
INPUTS: Uma Tupla 'ponto' para o ponto da distancia, Uma lista 'lista' para a lista de pontos
OUTPUT: Retorna a distancia entre os pontos de entrada
'''
def distLista(ponto, lista):
    if lista_vazia(lista):
        return 0
    else: 
        return distPoint(ponto, first_list(lista)) + distLista(first_list(lista), rest_list(lista))


'''
FUNCAO GLOBAL PRINCIPAL DA QUESTAO A:
OBJETIVO: Calcula a distancia percorrida por um robo especifico
INPUTS: Uma Lista 'l' com as informacoes do robo
OUTPUT: Retorna a distancia percorrida
'''

def distPercorridaRobo(ID_robo_alvo, lista_geral):
    try:
        if lista_vazia(gera_lista_robo_alvo(ID_robo_alvo, lista_geral)):
            raise exeception()
        else:    
            return distLista((0,0), gera_lista_Locate(gera_lista_robo_alvo(ID_robo_alvo, lista_geral)))
    except:
        print('ID do robo inexistente!!')
        pass

'''==============================================================================================================''
* * * * * *
* PARTE B *
* * * * * *
'''

'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'B':
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
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'B':
OBJETIVO: Funcao que mostra o robo que percorreu a maior distancia
INPUTS: lista de entrada geral
OUTPUT: A distancia e o ID do robo "mais cansado"
'''
def robo_maior_dist(lista_geral):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DA FUNCAO 'robo_maior_dist':
    OBJETIVO: Funcao que calcula e retorna a maior distancia junto com o robo correspondente
    INPUTS: lista com as distancias finais de cada robo e o robo correspondente
    OUTPUT: A distancia e o ID do robo
    ''' 
    def maior_dist(a, b):
        if a[1] >= b[1]:
            return a
        else:
            return b
        
    lista_gerada = gera_lista_robo_alvo(first_list(reduce(maior_dist, dist_end(lista_geral, retira_repetidos(gera_lista_robo(lista_geral))))), lista_geral)
    return (get_ID(lista_gerada), gera_lista_Locate(lista_gerada), lista_gerada[-1][1])

'''==============================================================================================================''
* * * * * *
* PARTE C *
* * * * * *
'''

'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE FUNCAO 'ordenaPontos':
OBJETIVO: Funcao que retorna organiza o formato de saida geral
INPUTS: Lista de IDs e a lista geral
OUTPUT: Id do robo, a distancia e a lista de pontos de cada robo
'''
def inf_All_IDs(lista_IDs, lista_geral):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DE FUNCAO 'inf_All_IDs':
    OBJETIVO: Funcao que retorna organiza o formato de saida de um robo
    INPUTS: Id do robo e a lista geral
    OUTPUT: Id do robo, a distancia e a lista de pontos
    '''
    def organiza_inf_ID(ID_robo_alvo, lista_geral):
        return (ID_robo_alvo, distPercorridaRobo(ID_robo_alvo, lista_geral), [(0,0)] + gera_lista_Locate(gera_lista_robo_alvo(ID_robo_alvo, lista_geral)))

    if lista_vazia(lista_IDs): 
        return []
    else: 
        return [organiza_inf_ID(first_list(lista_IDs), lista_geral)] + inf_All_IDs(rest_list(lista_IDs), lista_geral)

'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DE FUNCAO 'ordenaPontos':
OBJETIVO: Funcao que ordena
INPUTS: Lista geral
OUTPUT: A lista das distâncias ordenadas
'''
def jordana_sort(lista):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DE FUNCAO 'jordana_sort':
    OBJETIVO: Funcao que coloca um elemento na lista de forma ordenada 
    INPUTS: Elemento e a lista geral
    OUTPUT: A lista com o elemento ordenado
    '''
    def ajuda_jordana(n, lista):
        if lista_vazia(lista): return [n]
        elif second_list(n) > second_list(first_list(lista)): return [first_list(lista)] + ajuda_jordana(n, rest_list(lista))
        else: return [n] + lista

    if lista_vazia(lista): return []
    else: return ajuda_jordana(first_list(lista), jordana_sort(rest_list(lista)))

'''
FUNCAO GLOBAL PRINCIPAL DA QUESTAO 'C':
OBJETIVO: Ordena de forma crescente os robos e printa os pontos
INPUTS: Uma lista geral
OUTPUT: Retorna uma lista de tuplas em ordem crescente pelo ID.
'''
def ordenaPontos(lista_geral):
    return jordana_sort(inf_All_IDs(retira_repetidos(gera_lista_robo(lista_geral)), lista_geral))


'''==============================================================================================================''
* * * * * *
* PARTE D *
* * * * * *
'''

'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'D':
OBJETIVO: Funcao que calcula e retorna a soma do numero de pessoas
INPUTS: Uma lista 'lista_alvo' com os numeros a serem somados
OUTPUT: O somatorio de todos os elementos da lista
'''
def somatorio(lista_alvo):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DA FUNCAO 'somatorio':
    OBJETIVO: Funcao que calcula e retorna a soma entre dois numeros
    INPUTS: Um int 'x' para o numero 1 e outro int 'y' para o numero 2
    OUTPUT: A soma entre os dois numeros
    '''
    def soma(x, y):
        return x + y

    return reduce(soma, lista_alvo)


'''
FUNCAO GLOBAL AUXILIAR PARAMETRICA DA QUESTAO 'D':
OBJETIVO: Funcao que calcula e retorna a soma do numero de pessoas para cada robo da entrada
INPUTS: Uma lista 'lista_robos' com os robos de entrada e outra lista 'lista_geral' com as informacoes gerais de entrada
OUTPUT: Uma lista de tuplas com o primeiro elemento da tupla sempre indicando o ID do robo e o segundo elemento incando o total de pessoas avistadas
'''
def total_pessoas(lista_robos, lista_geral):
    if lista_vazia(lista_robos):
        return []
    else:
        return [(first_list(lista_robos), somatorio(gera_lista_People(gera_lista_robo_alvo(first_list(lista_robos), lista_geral))))] + total_pessoas(rest_list(lista_robos), lista_geral)


'''
FUNCAO GLOBAL PRINCIPAL PARAMETRICA QUESTAO 'D':
OBJETIVO: Funcao que calcula e retorna o robo que mais avistou vitimas juntamente com o numero de vitimas
INPUTS: Uma lista 'lista_geral' com as informacoes gerais de entrada
OUTPUT: Retorna o ID do robo que mais avistou, se existe mais de um robo que avistou a mesma quantidade se retorna uma lista com os IDs dos robos
'''
def robo_heroi(lista_geral):
    '''
    FUNCAO LOCAL AUXILIAR PARAMETRICA DA FUNCAO 'robo_heroi':
    OBJETIVO: Funcao que calcula e retorna o(s) robo(s) que avistou(aram) o maior numero de pessoas
    INPUTS: lista com o numero total de pessoas avistadas de cada robo e o robo correspondente
    OUTPUT: O ID do(s) robo(s) que avistou(aram) o maior numero de vitimas
    ''' 
    def maior_people(a, b):
        if type(a) == list:
            return maior_people(a[1], b)
        elif a[1] == b[1]:
            return [a, b]
        elif a[1] >= b[1]:
            return a
        else:
            return b
    
    robo_heroi = reduce(maior_people, total_pessoas(retira_repetidos(gera_lista_robo(lista_geral)), lista_geral))
    if type(robo_heroi) == list:
        return gera_lista_robo(robo_heroi)
    else:
        return first_list(robo_heroi)


'''========================================= FORMATACAO DE SAIDAS ========================================='''
# LISTA DE ENTRADA PARA AS FUNCOES
lista = [('robo1', 1, (5, 8), 4), ('robo2', 2, (5, 4), 4), ('robo3', 3, (2, 2), 1), ('robo1', 4, (4, 9), 4), ('robo3', 5, (1, 3), 3), ('robo4', 6, (7, 5), 3), ('robo5', 7, (8, 6), 1), ('robo1', 8, (3, 2), 4), ('robo2', 9, (1, 8), 4)]

# QUESTAO A)
print(distPercorridaRobo('robo1', lista))
# QUESTAO B)
print(robo_maior_dist(lista))
# QUESTAO C)
print(ordenaPontos(lista))
# QUESTAO D) 
listateste = [('robo1', 1, (5, 8), 4), ('robo3', 2, (4,2), 4)] # Para testar quando o numero de pessoas for igual
print(robo_heroi(lista))