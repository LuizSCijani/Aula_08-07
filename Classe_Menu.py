from Classe_Compra import *
from Classe_Venda import Venda


class Menu:
    def __init__(self):
        estoque_prod = Estoque()
        compra = Compra()
        venda = Venda()

        venda.entrada = estoque_prod
        compra.entrada = estoque_prod

        ##iniciar menu
        while True:
            print('Menu de operações'
                  '\n1 - Cadastrar fabricante'
                  '\n2 - Cadastrar produtos'
                  '\n3 - Listar todos'
                  '\n4 - Procurar produto'
                  '\n5 - Alterar produto'
                  '\n6 - Entrada de Produtos'
                  '\n7 - Saida de Produtos'
                  '\n0 - Sair')
            entrada = input('Informe a operação desejada: ')

            if entrada == '1':
                cod = None
                nome = input('Informe o nome: ')
                cnpj = input('informe o cnpj: ')
                estoque_prod.cadastro_fabct(cod, nome, cnpj)

            elif entrada == '2':
                cod = None
                id_fabct = input('Informe o id do fabricante: ')
                nome = input('Informe o nome: ')
                quat = input('Informe a quantidade: ')
                estoque_prod.cadastro_prod(cod, id_fabct, nome, quat)

            elif entrada == '3':
                estoque_prod.lista_produtos()

            elif entrada == '4':
                estoque_prod.lista_codp()

            elif entrada == '5':
                cod = input('Informe o codigo do produto: ')
                valor = input('Informe o novo nome: ')
                atributo = 'nome'
                estoque_prod.alterar_nome(cod, valor, atributo)

            elif entrada == '6':
                compra.comprar()

            elif entrada == '7':
                venda.vender()

            elif entrada == '0':
                break
            else:
                print('opção errada!')