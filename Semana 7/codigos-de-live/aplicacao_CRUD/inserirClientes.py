from listaDeClientes import listaClientes

from solicitarDadosClientes import solicitarDadosClientes


def inserirClientes(dicionario):
    cliente = solicitarDadosClientes()
    dicionario["nome"] = cliente[0]
    dicionario["CPF"] = cliente[1]
    listaClientes.append(dicionario)
    print(listaClientes)
