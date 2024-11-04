from modelos.cardapio.item_cardapio import ItemCardapio;

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    @property
    def tamanho(self):
        return self._descricao

    def __str__(self):
        return f'Prato: {self.nome} - R$ {self.preco} - {self.descricao}'
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.08
