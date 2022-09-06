# Pilha de execução

def funcao1():
    print('Entrou na função 1.')


def funcao2():
    print('Entrou na função 2.')
    funcao1()


def funcao3():
    print('Entrou na função 3.')
    funcao2()


# Chamando a função
funcao3()

# Modelo de função recursiva
'''
def minhaFuncaoRecursiva():
    if condicaoDeParada:
        < bloco de código >
    else:
        minhaFuncaoRecursiva()
'''

# Fatorial
'''
3! = 3 * 2!
2! = 2 * 1!
1! = 1 * 0!
0! = 1
'''

def fatorial(numero):
    if numero == 0:
        return 1
    resultado = numero * fatorial(numero - 1)
    return resultado


# Chamando a função
print(fatorial(3))
