from models import Item, session
from time import sleep




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
            quantidade = int(input("Quantidade: "))
            item = session.query(Item).filter_by(id=id_item).first()

            if item is None:
                print("Item não encontrado.")
                sleep(1)
                continue

            try:
                item.aumentar_estoque(quantidade)
                session.commit()
                print("Estoque atualizado com sucesso!")
            except ValueError as e:
                session.rollback()
                print("Erro ao atualizar o estoque:", str(e))
            
        elif opcao == 4:
            id_item = int(input("ID do item: "))
            quantidade = int(input("Quantidade: "))
            item = session.query(Item).filter_by(id=id_item).first()

            if item is None:
                print("Item não encontrado.")
                sleep(1)
                continue

            try:
                item.diminuir_estoque(quantidade)
                print("Estoque atualizado com sucesso!")
                session.commit()
            except ValueError as e:
                session.rollback()
                print("Erro ao atualizar o estoque:", str(e))

        elif opcao == 5:
            print("Saindo do programa...")
            sleep(1)
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
        print(f"ID: {item.id} | Categoria: {item.categoria} | Nome: {item.nome} | Quantidade: {item.quantidade} | Data: {item.data.strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 20)


menu_principal()
session.close()



    

    