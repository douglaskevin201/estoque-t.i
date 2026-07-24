from models import Item

itens = []


def menu():
    print("\nEstoque T.I UniEnsino")
    print("1 - Cadastrar um novo item ")
    print("2 - Listar itens")
    print("3 - Aumentar estoque")
    print("4 - Diminuir estoque")
    print("5 - Sair")
    return int(input("Escolha uma opcao: "))


def menu_principal():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_item()

        elif opcao == 2:
            listar_itens()

        elif opcao == 3:
            id_item = int(input("ID do item: "))
            quantidade = int(input("Quantidade"))
            for item in itens:
                if item.id == id_item:
                    item.aumentar_estoque(quantidade)
                    encontrado = True
                    break
                if not encontrado:
                    print

        elif opcao == 4:
            id_item = int(input("ID do item: "))
            quantidade = int(input("Quantidade: "))
            for item in itens:
                if item.id == id_item:
                    item.diminuir_estoque(quantidade)
                    encontrado = True
                    break
                if not encontrado:
                    print("Item nao encontrado!")

        elif opcao == 5:
            break


def cadastrar_item():
    id = int(input("ID: "))
    categoria = input("Categoria: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))
    data = input("Data de cadastro: ")

    novo_item = Item(id, categoria, nome, quantidade, data)
    itens.append(novo_item)



def listar_itens():
    if not itens:
        print("Nenhum Item encontrado")
        return
    print("\n--- ITENS NO ESTOQUE --- ")
    for item in itens:
        print(f"ID: {item.id} | Categoria: {item.categoria} | Quantidade: {item.quantidade} | Data: {item.data_cadastro}")
    print("-" * 20)


menu_principal()


    





    