# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetorA = list(range(1, 11))
vetorB = ['um', 'dois', 'tres', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez']
vetorC = []

for index in range(10):
    vetorC.append(vetorA[index])
    vetorC.append(vetorB[index])

print(vetorC)

# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# "Conhecia a vitima?""
#
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

vetorRespostas = []

vetorRespostas.append(input('Telefonou para a vítima? s/n\t'))
vetorRespostas.append(input('Esteve no local do crime? s/n\t'))
vetorRespostas.append(input('Mora perto da vítima? s/n\t'))
vetorRespostas.append(input('Devia para a vítima? s/n\t'))
vetorRespostas.append(input('Conhecia a vitima? s/n\t'))
vetorRespostas.append(input('Já trabalhou com a vítima? s/n\t'))


contadorSim = 0
contadorNao = 0

# ou contadorSim = vetorRespostas.count("s") contadorNao = vetorRespostas.count("n")

for resposta in vetorRespostas:
    if resposta == 's':
        contadorSim += 1
    elif resposta == 'n':
        contadorNao += 1


print(contadorSim)
print(contadorNao)
