'''Crie um programa que solicite ao usuário vários números e, ao digitar 0,
calcule a média dos números informados.'''

contador = 0
soma = 0

while True:
    num = int(input("Digite um número (0 para encerrar): "))
    if num == 0:
        break
    else:
        contador += 1
        soma += num
if contador == 0:
    print("Não foram inseridos números a calcular.")
else:
    media = soma / contador
    print(f"A média dos {contador} números é {media}.")

