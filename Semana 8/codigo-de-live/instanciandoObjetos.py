from Pessoa import Pessoa
from Biscoito import Biscoito

# Instanciando objetos da classe Pessoa
pessoa1 = Pessoa('Lyene', 29)
pessoa2 = Pessoa('Wilian', 32)

# Imprimindo as informações acerca dos objetos instanciados
pessoa1.imprimir()
pessoa2.imprimir()


# Instanciando objetos da classe Biscoito
bolacha1 = Biscoito('chocolate', 'marrom')
bolacha1.setTamanho('grande')
bolacha2 = Biscoito('morango', 'rosa')

# Imprimindo as informações acerca dos objetos instanciados
bolacha1.imprimir()
bolacha2.imprimir()

# Alterando os valores do objeto
bolacha1.alterar_registro('limão', 'marrom')
bolacha1.setTamanho('médio')

# Imprimindo as informações do objeto alterado
bolacha1.imprimir()
