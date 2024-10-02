
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca','Gourmet')

restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('ser',8)

def main():
    Restaurante.listar_restaurantes()



if __name__ == "__main__":
    main()