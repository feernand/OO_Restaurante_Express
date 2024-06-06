# criar uma classe Restaurante usando construtor
class Carros:
    carros=[]

    def __init__(self,modelo,cor,ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano

        Carros.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    #criar método para listar os restaurantes
    def listcarros():
        for carro in Carros.carro:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

# criação de objetos
carro_Fiat=Carros('Uno','branco','2010')

carro_Honda=Carros('Fit','vermelho','2015')


# 3 consumindo os objetos

print(vars(carro_Fiat))
print(vars(carro_Honda))
print('')

print(carro_Fiat)
print(carro_Honda)
print('')

# 5 consumindo o método li