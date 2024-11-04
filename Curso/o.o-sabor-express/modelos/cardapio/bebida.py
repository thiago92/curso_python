from modelos.cardapio.item_cardapio import ItemCardapio;

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    @property
    def tamanho(self):
        return self._tamanho

    def __str__(self):
        return f'Bebida: {self.nome} - R$ {self.preco} - {self.tamanho}'
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.05