print("Seja bem-vindo!")
nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
aniversario = input("Você já fez aniversário esse ano? (s/n)")

ano_atual = 2022

idade = ano_atual - ano_nascimento

if aniversario == 's' or 'S':
    print("Sua idade é: ", idade)
else:
    print("Sua idade é: ", idade - 1)

