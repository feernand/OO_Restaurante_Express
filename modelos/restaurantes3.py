# criar um decorator @property
class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._status=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._status}'

    #criar método para listar os restaurantes
    def listar_restaurantes(cls):

        print(f'{'nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante._status}')

    @property
    def status(self):
        return '⊠' if self._status else '⊗'

    def alterar_estado(self):
        self._status=not self._status
# criação de objetos
restaurante_praca=Restaurante('praça','Gourmet')
restaurante_praca._nome='biqueira'

restaurante_pizza=Restaurante('pizza express','Italiana')


# 3 consumindo os objetos

print(vars(restaurante_praca))
print(vars(restaurante_pizza))
print('')

print(restaurante_praca)
print(restaurante_pizza)
print('')

# 5 consumindo o método li