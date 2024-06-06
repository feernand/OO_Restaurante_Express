# 1 importar o arquivo que contém a classe Restaurante
from modelos.restaurantes4 import Restaurante

#4 criar um objeto(instancial de restaurante)
restaurante_praca=Restaurante('praca','gourmet')
restaurante_mexicando=Restaurante('mexican food','mexicano')
restaurante_japones=Restaurante('japa','japones')

#alternar estado de um restaurante
restaurante_japones.alterar_estado()

# criando avaliações para o restaurante praça
restaurante_praca.receber_avaliacao('anonimo',8.5)
restaurante_praca.receber_avaliacao('Ana Maria',7)
restaurante_praca.receber_avaliacao('Gelson',8)

restaurante_mexicando.receber_avaliacao('alberto',8)
restaurante_mexicando.receber_avaliacao('Maria',7.5)
restaurante_mexicando.receber_avaliacao('Cladio',8)

restaurante_japones.receber_avaliacao('Clara',8.5)
restaurante_japones.receber_avaliacao('Lamar',9)
restaurante_japones.receber_avaliacao('whong',8)

#2 criando a chamada da função de entrada
def main():
    # 5 inserir um ação dentro do main
    Restaurante.listar_restaurantes()

if __name__=='__main__':
    main()