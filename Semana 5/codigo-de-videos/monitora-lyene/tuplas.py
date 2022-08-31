numeros = (25, 33, 29, 45, 62, 29)
print(numeros)

tuplaHeterogenea = (5, 'oi', 2.3, True)
print(tuplaHeterogenea)

# Conta a quantidade de elementos
print(f'A tupla tem {len(numeros)} elementos.')

# Pesquisa quantos elementos a tupla tem de determinado valor
print(f'A tupla tem {numeros.count(29)} valores iguais a 29.')

# Procura em qual posição aparece o valor pela primeira vez
print(f'O número 29 está na posição {numeros.index(29)}.')

# Utilizando laço de repetição com tupla
for i in range(len(numeros)):
    print(numeros[i])

# Gera erro porque os valores da tupla são imutáveis
# numeros[0] = 5

# Gera erro porque a função append não existe para tuplas, fazendo parte das listas
# numeros.append(5)

# Lista dentro de tupla
listaNumeros = ([1, 2, 3], [5, 6, 7])
print(listaNumeros)
# Adicionando elementos às listas
listaNumeros[0].append(4)
listaNumeros[1]. append(8)
print(listaNumeros)

# Concatenação de tupla
tupla1 = ('Raciocínio',)
print(tupla1)
tupla2 = ('Computacional',)
print(tupla2)
tupla3 = tupla1 + tupla2
print(tupla3)
tupla1 += tupla2
print(tupla1)
