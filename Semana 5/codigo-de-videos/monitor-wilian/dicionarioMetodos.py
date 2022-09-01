dicionario1 = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 3,
    'chave4': True,
}


# metodo keys() para pegar todas as chaves do dicionario, retorna um dict_keys()

# chaves = dicionario1.keys()
# print(chaves)

# for chave in chaves:
#     print(chave)

# -------------------------------------------------------------------------------------

# metodo values() para pegar os valores das chaves, retorna dict_values

# valores = dicionario1.values()
# print(valores)

# for valor in valores:
#     print(valor)


# -------------------------------------------------------------------------------------

# metodo items() para retornar uma lista com tuplas com chave-valor, retorna dict_items

# listaPares = dicionario1.items()
# print(listaPares)

# novoDict = dict(listaPares)
# print(novoDict)

# for item in listaPares:
#     print(item)
#     print(type(item))

# -------------------------------------------------------------------------------------

# metodo fromKeys(iteravel, valor) popula um dicionario com as chaves de um iteravel no primeiro parametro, e insere como valor em todas as chaves o que estiver no segundo parametro.

# dicionario = {}
# novoDicionario = dicionario.fromkeys(dicionario1, False)
# print(novoDicionario)

# --------------------------------------------------------------------------------------

# metodo copy() retorna uma copia exata do dicionario em outra variavel.

# dicionarioCopia = dicionario1.copy()
# print(dicionarioCopia)

# stop
# --------------------------------------------------------------------------------------

# metodo clear() para limpar a estrutura dicionario, retorna None

# print(dicionario1.clear())
# print(dicionario1)

# --------------------------------------------------------------------------------------

# metodo get(chave) para pegar valor da chave, não retorna erro caso a chave não exista no dicionario, mas sim None

# valor = dicionario1.get("chave4")
# print(valor)

# --------------------------------------------------------------------------------------

# metodo update() para inserir novos pares chave-valor no final do dicionario se chave não estiver na lista, caso a chave estiver na lista com novo valor, o valor será atualizado

# dicionarioNovo = {"NovaChave": "NovoValor"}
# listaUpdate = [("chave4", False)]

# dicionario1.update(dicionarioNovo)
# dicionario1.update(listaUpdate)

# print(dicionario1)

# --------------------------------------------------------------------------------------

# metodo popitem() para pegar o ultimo par do dicionario e remove-lo

# retornoDicionario = dicionario1.popitem()
# print(retornoDicionario)
# print(dicionario1)

# --------------------------------------------------------------------------------------

# metodo pop() para pegar chave e valor especifico do dicionario a partir da chave e retira-lo do dicionario

# retornoDicionario = dicionario1.pop("chave2")
# print(retornoDicionario)
# print(dicionario1)
