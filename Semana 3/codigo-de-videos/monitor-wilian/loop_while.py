
contador = 1

while contador <= 10:
    print(f"O contador está em: {contador}")
    contador = contador + 1

    if contador == 5:
        print(f"Contador esta em {contador}, próximo")
        continue
    elif contador == 9:
        print(f"Contador em {contador}, vou sair do loop")
