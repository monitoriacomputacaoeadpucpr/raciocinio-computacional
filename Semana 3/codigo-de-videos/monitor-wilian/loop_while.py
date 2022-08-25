
contador = 1
somador = 0

while contador <= 10:
    print(f"O contador está em: {contador}")
    contador = contador + 1

    if contador == 5:
        print(f"Contador está em {contador}, próximo")
        continue
