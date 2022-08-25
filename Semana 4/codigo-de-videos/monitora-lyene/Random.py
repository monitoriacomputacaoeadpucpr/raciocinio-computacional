import random

nome = 'Lyene'
letraSorteada = random.choice(nome)
print(letraSorteada)

sorteio = []
for i in range(3):
    sorteio.append(random.choice(nome))
print(sorteio)

lista = ['Lyene', 'Wilian', 'Johnny', 'Joyce']
nomeSorteado = random.choice(lista)
print(nomeSorteado)
