# Função é um meio pelo qual podemos encapsular trechos de alguma funcionalidade do nosso código e evitar a repetição de trechos

# modulos


from operacoesMatematicas import funcaoMultiplicar, funcaoSomar

soma = funcaoSomar(2, 5)
print(soma)

multiplicacao = funcaoMultiplicar(34, 4352)
print(multiplicacao)


# escopo de função e escopo global

variavelX = 30


def funcaoSubtrair(a, b):
    variavelX = "trinta"
    return a - b, variavelX


resultadoSubtracao, segundoElem = funcaoSubtrair(variavelX, 15)

print(resultadoSubtracao)
print(variavelX)
print(segundoElem)


# precedencia de chamado, código sincrono e assincrono


def funcaoDivisao(a, b):
    return a / b


divisao = funcaoDivisao(4, 2)
print(divisao)


# parametros padrões

def trueOrFalse(booleano=True, booleano2=False):
    print(booleano == booleano2)


trueOrFalse(False, False)


# Boas práticas sobre função segundo o Livro "Clean Code" de Robert Cecil Martin, Tio Bob.

# Funções devem ser pequenas
# Funções devem fazer apenas uma coisa
# Funções devem ter nomes descritivos
# Funções deveriam ter poucos parametros
