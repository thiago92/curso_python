from modelos.restaurantes import Restaurante

restaurante_preca = Restaurante('Parça', 'executivos')

restaurante_preca.receber_avaliacao('João', 5)
restaurante_preca.receber_avaliacao('Maria', 4)
restaurante_preca.receber_avaliacao('José', 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()