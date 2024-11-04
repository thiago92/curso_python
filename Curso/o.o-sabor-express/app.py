from modelos.restaurantes import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_preca = Restaurante('Parça', 'executivos')
bebida_suco = Bebida('Suco de laranja', 5.00, '300ml')
bebida_suco.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 25.00, 'Feijoada completa')
prato_feijoada.aplicar_desconto()
restaurante_preca.add_no_cardapio(bebida_suco)
restaurante_preca.add_no_cardapio(prato_feijoada)

def main():
    restaurante_preca.exibir_cardapio

if __name__ == '__main__':
    main()