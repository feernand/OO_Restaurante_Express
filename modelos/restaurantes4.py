# 1 tornando

# import da class Avaliacao
from modelos.avalicao import Avalicao


class Restaurante:
    restaurantes=[]

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._avaliacao=[]
        self._status=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'notas'.ljust(20)} | {'status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante._status}')

    @property
    def status(self):
        return '⊠' if self._status else '⊗'

    def alterar_estado(self):
        self._status=not self._status

# criando um método para receber as avaliacao
    def receber_avaliacao(self,cliente,nota):
        avaliacao=Avalicao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas,1)
        return media


