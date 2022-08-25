'''
Elabore um programa que solicite ao usuário, separadamente, seu nome e sobrenome e mostre a mensagem:
“Seu nome completo: Nome Sobrenome.”, com um espaço na junção dos nomes e um ponto no final,
sem pular linha.
'''

nome = input("Por favor, digite o seu nome: ")
sobrenome = input("Por favor, digite o seu sobrenome: ")

# print(f'Seu nome completo: {nome} {sobrenome}.')

print('Seu nome completo: {} {}'.format(nome, sobrenome))