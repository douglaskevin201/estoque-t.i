


class Item:
    def __init__(self, id, categoria, nome, quantidade, data_cadastro):
        self.id = id
        self.categoria = categoria
        self.nome = nome
        self.quantidade = quantidade
        self.data_cadastro = data_cadastro

    def aumentar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Quantidade invalida!")
            raise ValueError("Numeros negativos não são permitidos.")
        else:
            self.quantidade += quantidade


    def diminuir_estoque(self, quantidade):
        if quantidade <= 0:
            print(f"Quantidade insuficiente no estoque. Qnt: {self.quantidade}")
            raise ValueError("Numeros negativos não são permitidos.")
        elif quantidade > self.quantidade:
            print(f"Quantidade insuficiente no estoque. Qnt {self.quantidade}")
            raise ValueError("Quantidade insuficiente em estoque.")
        else:
            self.quantidade -= quantidade

    
        

listar_itens = Item()
for itens in listar_itens:
    print(f"{self.id} - {self.nome} - {self.quantidade}")

