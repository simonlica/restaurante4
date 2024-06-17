from modelos.restaurante4 import Restaurante

restaurante1=Restaurante('Salgadinho sabor queijo','petisco')
restaurante2=Restaurante('Saco de feijão','feijoada')
restaurante3=Restaurante('Calabreo','massas')

restaurante3.alternar_status()
restaurante3.receber_avaliacao('ronaldo',4)
restaurante3.receber_avaliacao('Amanda',3)

def main():
    Restaurante.listar_restaurantes()

if __name__=='__name__':
    main()
