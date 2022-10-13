numero = 12.1111111111111111
frase = "A função format é massa"
booleano = True
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# A função print possui alguns parametros:

# print(*values, file=sys.stdout.write(), sep=" ", end="\n", flush=False)

# -values são os valores que voce deseja imprimir no console, parametro arbitrario
# -file é onde voce quer imprimir os valores, por padrão o python usa sys.stdout, uma função que mostra os que for passado no valor na tela do console, é possivel mudar esse argumento, por exemplo para criar um arquivo.arquivo

# função open cria e le arquivos, no primeiro parametro é o nome do arquivo a ser lido ou escrito, o segundo parametro "w+" indica que função criará o arquivo truncando o mesmo, ou seja, apagando o que estiver no arquivo caso ele ja exista. Mais detalhes https://docs.python.org/pt-br/3/library/functions.html#open

arquivo = open("temp.txt", "w+")
print(lista, file=arquivo, sep="")

# -sep é o separador dos valores, por padrão é espaço
# -end mostrado no final de cada linha, por padrão é \n
# -flush força o python imprimir de forma imediata os valores caso o parametro end for diferente do padrão

# -------------------------------------------------------------------------------------------


# Interpolação de variveis com sinal "%", usa-se o sinal "%" aonde gostaria de inserir a variavel e logo depois a letra "s" para inserir a variavel como string, f para "float" ou "i" para inteiros


# print("Primeiro exemplo: %s" % frase)
# print("Segundo exemplo: %s, %.2f, %s" % (frase, numero, booleano))
# print()

# -------------------------------------------------------------------------------------------

# A função format permite a formatação da string baseada em agumentos

# print("Primeiro exemplo: {} {:.2f}".format(lista, numero))

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in matriz:
#     print()
#     for j in i:
#         print("{:^7}".format(j), end=" ")

# print()
# -------------------------------------------------------------------------------------------


# A format string permite interpolar variaveis de uma forma mais legivel ao programador

print(f"\nPrimeiro Exemplo: {numero:.2f}\tSegundo exemplo: {lista}")
# -------------------------------------------------------------------------------------------
