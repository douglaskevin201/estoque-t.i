


class Item:
    def __init__(self, id, nome, quantidade, data_cadastro):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.data_cadastro = data_cadastro

    def aumentar_estoque(self, quantidade):
        self.quantidade += quantidade

    def diminuir_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            raise ValueError("Quantidade insuficiente em estoque.")
        

