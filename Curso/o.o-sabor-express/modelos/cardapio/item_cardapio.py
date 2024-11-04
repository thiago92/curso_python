from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        return self._preco
    
    @abstractmethod
    def aplicar_desconto(self):
        pass

