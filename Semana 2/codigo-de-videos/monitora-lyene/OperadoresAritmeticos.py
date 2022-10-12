# Criando variáveis e atribuindo valores a elas

numero1 = 25
numero2 = 2

operacao = input('Escolha uma operação (+ - * / %): ')


# Efetuar a operação escolhida pelo usuário

if operacao == '+':
    print(numero1 + numero2)
elif operacao == '-':
    print(numero1 - numero2)
elif operacao == '*':
    print(numero1 * numero2)
elif operacao == '/':
    print(numero1 / numero2)
else:
    print(numero1 % numero2)

