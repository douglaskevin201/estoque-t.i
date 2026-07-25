from models import Item, session




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
            item = session.query(Item).filter_by(id=id_item).first()
            if item:
                item.aumentar_estoque(quantidade)
                session.commit()

        elif opcao == 4:
            id_item = int(input("ID do item: "))
            quantidade = int(input("Quantidade: "))
            item = session.query(Item).filter_by(id=id_item).first()
            if item:
                item.diminuir_estoque(quantidade)
                session.commit()

        elif opcao == 5:
            break


def cadastrar_item():
    categoria = input("Categoria: ")
    nome = input("Nome: ")
    quantidade = int(input("Quantidade: "))

    novo_item = Item(categoria=categoria, nome=nome, quantidade=quantidade)
    session.add(novo_item)
    session.commit()



def listar_itens():
    itens = session.query(Item).all()
    if not itens:
        print("Nenhum Item encontrado")
        return 
    print("\n--- ITENS NO ESTOQUE --- ")
    for item in itens:
        print(f"ID: {item.id} | Categoria: {item.categoria} | Quantidade: {item.quantidade} | Data: {item.data}")
    print("-" * 20)


menu_principal()
session.close()


    





    