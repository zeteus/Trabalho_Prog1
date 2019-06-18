def teste(lista):
    return lista[0][1]


def gera_lista_Time(lista_alvo):
        if lista_alvo == []:
            return []
        else:
            return [teste(lista_alvo)] + gera_lista_Time(lista_alvo[1:])

lista_teste = [('robo3', 1, (7, 7), 3), ('robo4', 2, (7, 5), 2), ('robo3', 3, (5, 4), 3), ('robo3', 4, (8, 1), 4), ('robo4', 5, (4, 5), 3), ('robo5', 6, (7, 7), 4), ('robo5', 7, (6, 4), 5), ('robo3', 8, (7, 2), 3), ('robo5', 9, (6, 4), 4)]
print(lista_teste[:-1])