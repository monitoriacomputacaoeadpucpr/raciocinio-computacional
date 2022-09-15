from listaDeClientes import listaClientes
from menu import menu
from pesquisarCliente import pesquisarCliente


def editarClientes():
    cliente, index = pesquisarCliente()

    if cliente == False:
        menu()

    novoNome = input(
        "Achamos o cliente. Insira o novo nome para atualização: ")

    cliente["nome"] = novoNome
    listaClientes.pop(index)
    listaClientes.insert(index, cliente)
    print(listaClientes)
