import random

def sortear(variavel, numeroVezes):
    '''
    A função sortear(variavel, numeroVezes) sorteia um valor contido no parâmetro variavel pelo número de vezes indicado pelo segundo parâmetro.

    :param variavel: string ou lista da qual queremos sortear valores
    :param numeroVezes: número de repetições que o sorteio deve ser realizado
    '''

    sorteio = []
    for i in range(numeroVezes):
        sorteio.append(random.choice(variavel))
    print(sorteio)


sortear(['Lyene', 'Wilian', 'Johnny', 'Joyce'], 1)
sortear('Lyene', 3)
