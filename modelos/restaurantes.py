# criar uma classe Restaurante
class Restaurante:
    nome=''
    categoria='bar'
    status=False

# criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Restaurante Praça'
restaurante_praca.categoria='Bar'

restaurante_pizza=Restaurante()
restaurante_pizza.nome='Restaurante pizza'
restaurante_pizza.categoria='Pizzaria'
# questão 1

restaurantes=[restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))

nome_restaurante=restaurante_praca.nome
print(nome_restaurante)

# questão 1
restaurante_praca.categoria='Italiano'
print(restaurante_praca.categoria)
print('')

# questão 2
nome_restaurante=restaurante_praca.nome
print(nome_restaurante)
print('')

# questão 3
if restaurante_praca.status:
    print('O restaurante ',restaurante_praca.nome,' está ativo')
else:
    print('O restaurante ',restaurante_praca.nome,' está inativo')
print('')

# questão 4
categoria=Restaurante.categoria
print(categoria)

# questão 5
restaurante_praca.nome='Bistrô'
print(restaurante_praca.nome)
print('')

# questão 6
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
print(vars(restaurante_pizza))
print('')

# questão 7
if restaurante_pizza.categoria=='Fast Food':
    print('A categoria é fast food')
else:
    print('A categoria não é fast food')
print('')

# questão 8
restaurante_pizza.status=True
print(restaurante_pizza.status)
print('')

# questão 9
print(f'Nome: {restaurante_praca.nome}, categoria: {restaurante_praca.categoria}')