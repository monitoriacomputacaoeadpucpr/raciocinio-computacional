# Classe Pessoa

class Pessoa:

    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def imprimir(self):
        print(f'Este objeto da classe Pessoa tem os valores:\n{self.nome} referente ao atributo nome;\n{self.idade} '
              f'referente ao atributo idade.\n')

