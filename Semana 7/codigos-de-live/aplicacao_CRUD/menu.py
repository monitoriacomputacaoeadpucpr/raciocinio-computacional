def menu():
    print()
    print("***CLIENTES***")
    print("1. Inserir Cliente")
    print("2. Editar Cliente")
    print("3. Listar Clientes")
    print("4. Pesquisar Cliente")
    print("5. Excluir Cliente")
    print("6. Sair\n")

    operacao = int(input("Escolha uma das opções: "))

    if 1 <= operacao <= 6:
        return operacao
    else:
        print("Opção invalida")
