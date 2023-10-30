def busca(lista, elem):
    """Retorna o indice do elemento se ele estiver na lista ou None, caso contrario"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = 5

indice = busca(lista, elemento)
if indice is not None:
    print(f'O indice do elemente {elemento} é {indice}')
else:
    print(f"O elemento {elemento} não está na lista")