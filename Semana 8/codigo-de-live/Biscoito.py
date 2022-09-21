# Classe Biscoito (ou Bolacha), como preferir (risos)

class Biscoito:

    tamanho = 'pequeno'

    # Método construtor
    def __init__(self, sabor, cor):
        self.sabor = sabor
        self.cor = cor


    def setTamanho(self, tamanho):
        self.tamanho = tamanho


    def alterar_registro(self, sabor, cor):
        self.sabor = sabor
        self.cor = cor


    def imprimir(self):
        print(f'Este objeto da classe Biscoito tem os valores:\n{self.sabor} referente ao atributo sabor;\n{self.cor} '
              f'referente ao atributo cor;\n{self.tamanho} referente ao atributo tamanho.\n')

