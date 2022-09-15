"""
Módulo de cadastro de clientes
"""
from deletarCliente import deletarCliente
from editarClientes import editarClientes
from inserirClientes import inserirClientes
from listarClientes import listarClientes
from menu import menu
from pesquisarCliente import pesquisarCliente


def inicioClientes():

    while True:
        operacao = menu()
        match operacao:
            case 1:
                inserirClientes({})
            case 2:
                editarClientes()
            case 3:
                listarClientes()
            case 4:
                pesquisarCliente()
            case 5:
                deletarCliente()
            case 6:
                break


inicioClientes()
