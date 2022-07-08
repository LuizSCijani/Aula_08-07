from Classe_Fabricante import *

class Produtos:
    def __init__(self, codigo, nome, id_fabct, quantidade=0):
        self.cod = codigo
        self.nome = nome
        self.id_fabct = id_fabct
        self.quat = quantidade
