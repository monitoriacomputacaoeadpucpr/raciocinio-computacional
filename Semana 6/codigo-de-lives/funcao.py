# Imprimir na tela "Miau" 3 vezes
print('Miau')
print('Miau')
print('Miau')

# Pula linha
print()

# Melhorando com laço de repetição
for i in range(3):
    print('Miau')

# Pula linha
print()

# Melhorando com função
# Definindo a função
def printMiau():
    """
    A função printMiau() imprime "Miau" na tela 3 vezes
    """

    for i in range(3):
        print('Miau')


# Chamando a função
printMiau()

# Pula linha
print()

# Melhorando a função
# Definindo a função
def printMiau2(numeroVezes):
    """
    A função printMiau2(numeroVezes) imprime "Miau" pelo númro de vezes indicado no parâmetro

    :param numeroVezes: quantas vezes deve imprimir "Miau"
    """

    for i in range(numeroVezes):
        print('Miau')


# Chamando a função
printMiau2(3)

# Pula linha
print()

# Definindo função com retorno
def somar(num1, num2):
    """
    A função somar(num1, num2) realiza a soma dos dois números passados por parâmetro e retorna o resultado da operação

    :param num1: parcela a ser somada
    :param num2: outra parcela a ser somada
    :return: retorna o resultado da adição
    """

    soma = num1 + num2
    return soma


# Chamando a função
resultado = somar(1, 2)
print(resultado)

print(somar(2, 2))

# Parâmetros arbitrários - forma uma tupla
def somar2(*numeros):
    """
    A função somar2(*numeros) realiza a soma dos números passados por parâmetro e retorna o resultado da operação

    :param numeros: parcelas a serem somadas
    :return: retorna o resultado da adição
    """

    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
    return soma

# Chamando a função
print(somar2(2, 5, 3, 5))
