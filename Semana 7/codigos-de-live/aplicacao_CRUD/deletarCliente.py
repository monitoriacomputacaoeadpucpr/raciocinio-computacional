from listaDeClientes import listaClientes
from menu import menu
from pesquisarCliente import pesquisarCliente


def deletarCliente():
    cliente, index = pesquisarCliente()
    controle = input(f"Deseja excluir cliente {cliente['nome']}? - y/n ")

    if controle == "y":
        listaClientes.pop(index)
    else:
        menu()
