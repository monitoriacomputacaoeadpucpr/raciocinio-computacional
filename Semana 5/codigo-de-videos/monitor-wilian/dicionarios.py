# Dicionario é uma estrutura de dados baseada em chave-valor, onde chave pode ser qualquer tipo menos outras estruturas, e valor pode ser qualquer tipo inclusive estruturas. Mutavel.

dicionario1 = {}

dicionario1["chave1"] = "valor1"
dicionario1["chave2"] = "valor2"
dicionario1["chave3"] = "valor3"
dicionario1["4"] = 4
dicionario1["chave5"] = True
dicionario1["chave6"] = ["aaa", "bbb"]
dicionario1["chave7"] = ("aaa", "bbb")
dicionario1["chave8"] = {"subchave": "subvalor"}
dicionario1[9] = 9
dicionario1[True] = True

for item in dicionario1:
    print(item)

tipo1 = type(dicionario1["chave6"])
tipo2 = type(dicionario1["chave7"])
tipo3 = type(dicionario1["chave8"])

print(tipo1)
print(tipo2)
print(tipo3)

dicionario1["chave3"] = "valor333333"

print(dicionario1["chave3"])

temChaveDicionario = "4" in dicionario1
temValorDicionario = "valor333333" in dicionario1.values()

print(temChaveDicionario)
print(temValorDicionario)

array1 = [("aaa", "bbb"), ("ccc", "ddd")]
dicionario2 = dict(array1)

print(dicionario2)
