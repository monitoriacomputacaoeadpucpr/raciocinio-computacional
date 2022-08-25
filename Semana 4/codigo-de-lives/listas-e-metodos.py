# declaração de listas
# lista1 = []
# lista2 = list(range(1, 11))

# print(lista1)
# print(lista2)
# -----------------------------------------------------------------------------------------------
# indice e indice invertido

# lista1 = [1, 2, 3, 4, 5]
# #         0, 1, 2, 3 ,4  -> index
# #        -5,-4,-3,-2,-1  -> index reverso

# print(lista1[-1])  # Pega o ultimo item de um array
# print(lista1[0])  # Pega o primeiro item de um array
# -----------------------------------------------------------------------------------------------
# in para verificar se há item em lista

# lista1 = ['Um', 'Dois', 'Tres']  # Case Sensitive

# temItem = 'um' in lista1
# print(temItem)
# -----------------------------------------------------------------------------------------------
# concatenação de listas com +

# lista1 = ['Um', 'Dois', 'Tres']
# lista2 = [1, 2, 3]

# novaLista = lista2 + lista1
# print(novaLista)
# -----------------------------------------------------------------------------------------------
# metodo len(lista) para verificar a quantidade de itens dentro de uma lista
# lista1 = [1, 2, 3]
# lengthLista1 = len(lista1)

# print(lengthLista1)
# -----------------------------------------------------------------------------------------------
# metodo append(item) para adicionar um elemento ao final da lista
# lista1 = [1, 2, 3]
# lista1.append('Um')

# print(lista1)
# -----------------------------------------------------------------------------------------------
# metodo insert(index, item) para adicionar item em indice especifico na lista
# lista1 = [1, 2, 3]
# lista1.insert(2, 'TRES')

# print(lista1)
# -----------------------------------------------------------------------------------------------
# metodo pop() ou pop(index) remove o ultimo item da lista e retorna-o

# lista1 = [1, 2, 3]
# lista1.insert(2, 'TRES')

# print(lista1)

# lista1.pop(0)

# print(lista1)
# -----------------------------------------------------------------------------------------------
# metodo sort(reverse=True|False) para ordenar uma lista de "a" a "z" e ordem crescente por padrão

# lista1 = [1, 2, 3, 7, 3, 5, 7, 3, 2, 0]

# lista1.sort(reverse=True)

# print(lista1)
# -----------------------------------------------------------------------------------------------
# metodo set() elimina itens duplicados dentro da uma lista

# lista1 = [1, 2, 3, 7, 3, 5, 7, 3, 2, 0]
# print(lista1)

# lista2 = set(lista1)
# print(lista2)
# -----------------------------------------------------------------------------------------------
# metodo count(item) retorna o numero de vezes que determinado item aparece na lista

# lista1 = [1, 2, 3, 7, 3, 5, 7, 3, 2, 0]

# quantidadeItem = lista1.count(7)
# print(quantidadeItem)
# -----------------------------------------------------------------------------------------------
# metodo Counter() do modulo collections, retorna um dicionario com o numero de ocorrencias de cada item dentro do array.
# import collections

# lista_nomes = ['Maria', 'João', 'Maria', 'Paulo', 'João', 'Maria', 'Cláudia']
# ocorrencias = collections.Counter(lista_nomes)

# print(ocorrencias)
#
# -----------------------------------------------------------------------------------------------
# min, max e sum

# lista1 = [1, 2, 3, 7, 3, 5, 7, 3, 2, 0]

# maxLista1 = max(lista1)
# minLista1 = min(lista1)
# sumLista1 = sum(lista1)

# print(maxLista1)
# print(minLista1)
# print(sumLista1)
