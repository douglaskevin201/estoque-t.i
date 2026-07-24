


class Item:
    def __init__(self, id, categoria, nome, quantidade, data_cadastro):
        self.id = id
        self.categoria = categoria
        self.nome = nome
        self.quantidade = quantidade
        self.data_cadastro = data_cadastro

    def aumentar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        else:
            self.quantidade += quantidade


    def diminuir_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Numeros negativos não são permitidos.")
        elif quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        else:
            self.quantidade -= quantidade

    def exibir_dados(self):
        return f"ID: {self.id} | Categoria: {self.categoria} | Nome: {self.nome} | Quantidade: {self.quantidade} | Cadastrado: {self.data_cadastro}"



