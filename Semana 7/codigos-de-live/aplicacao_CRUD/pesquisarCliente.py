from listaDeClientes import listaClientes


def pesquisarCliente():
    cpf = input("Insira o número de CPF que deseja encontrar: ")
    index = 0
    for item in listaClientes:

        if item["CPF"] == cpf:
            print(item)
            return item, index

        index += 1

    return False


if __name__ == "__main__":
    pesquisarCliente()
