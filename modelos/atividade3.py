# class Livro:
#     def __init__(self,titulo,autor,paginas):
#         self.titulo=titulo
#         self.autor=autor
#         self.paginas=paginas
#     def __str__(self):
#         return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

#     @property
#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def titulo_autor(self):
#         return f'{self.titulo} por {self.autor}'

#     def aumentar_paginas(self,quantidade):
#         self.paginas += quantidade

# livro1=Livro('tanto faz e abacaxi','Reinaldo Moraes',50)
# print(livro1)
# print('')

# livro1.aumentar_paginas(90)
# print(livro1)
# print('')
# print('')

# # questão 1

# class Pessoa:
#     def __init__(self,nome,idade,profissao):
#         self.nome=nome
#         self.idade=idade
#         self._profissao=profissao

#     def __str__(self):
#         return f'{self.nome}, {self.idade} anos, {self._profissao}'

#     @property
#     def saudacao(self):
#         if self._profissao:
#             return print(f'Olá, sou {self.nome}! Trabalho como {self._profissao}.')
#         else:
#             print (f'Olá, sou {self.nome}')

#     def aniversario(self):
#         self.idade +=1

# pessoa1=Pessoa('MC Zoio de gato',16,'Funkeiro')
# print(pessoa1)
# print('')

# pessoa1.aniversario()
# print(pessoa1)
# print('')

# pessoa1.saudacao()
# print(pessoa1)
# print('')

# questão2

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        self._ativa=True  #atributo protegido

# questão 3
    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'

# conta1=ContaBancaria('Karim Benzema',2.50)
# conta2=ContaBancaria('Neymar Jr.',1.82)

# print(conta1)
# print('')
# print(conta2)

# questão 4
#     @classmethod
#     def ativar_conta(cls,conta):
#         conta3._ativo=False

# conta3=ContaBancaria('Cristiano Ronaldo',1.43)
# print(f'Antes de ativar: conta ativa? {conta3._ativa}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativar: conta Ativa? {conta3._ativa}')

# questão 5
# class ContaBancariaPythonica:
#     def __init__(self,titular,saldo):
#         self._titular=titular
#         self._saldo=saldo
#         self._ativo=False

#     @property
#     def titular(self):
#         return self._titular
    
#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo
    
# # questão 6
# conta4=ContaBancariaPythonica('Leonel Messi', 4.12)
# print(f'Titular da conta 4 é: {conta4.titular}')

#questão 7
class ClienteBanco:
    def __init__(self,nome,idade,profissao,endereco,telefone):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        self.endereco=endereco
        self.telefone=telefone

# cliente1=ClienteBanco('Yudi Tamashiro',31,'Apresentador de televisão e cantor','Avenida Paulista, 147','4402-8922')
# cliente2=ClienteBanco('Yudi Tamashiro',31,'Apresentador de televisão e cantor','Avenida Paulista, 147','4402-8922')
# cliente3=ClienteBanco('Yudi Tamashiro',31,'Apresentador de televisão e cantor','Avenida Paulista, 147','4402-8922')

# questão 8

    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return
    
conta_cliente1=ClienteBanco.criar_conta('Tereza', 120000000000.00)
print(f'Conta de {conta_cliente1.titular} com saldo se R${conta_cliente1.saldo_inical}')
