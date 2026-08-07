from models import Item, Item_hardware, session
from time import sleep
from sqlalchemy.exc import SQLAlchemyError






def menu():
    while True:
        try:
            print("\nEstoque T.I UniEnsino")
            print("1 - Cadastrar um novo item ")
            print("2 - Listar itens")
            print("3 - Aumentar estoque")
            print("4 - Diminuir estoque")
            print("5 - Apagar item do estoque")
            print("6 - Sair")
            opcao = int(input("Escolha uma opcao: "))
            if 1 <= opcao <= 6:
                return opcao
            else:
                print("Opção invalida. Escolha um número entre 1 e 6.")
        except ValueError:
            print("Entrada inválida. Digite o número da opção.")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Saindo.")
            return 6



def menu_principal():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastrar_item()

        elif opcao == 2:
            listar_itens()

        elif opcao == 3:

            while True:
                try:
                    id_item = int(input("ID do item: "))
                    quantidade = int(input("Quantidade: "))                    
                    break

                except ValueError:
                    print("Digite somente numeros inteiros!")
                    continue
                
            item = session.query(Item).filter_by(id=id_item).first()    
            if item is None:
                print("Item não encontrado.")
                                                                                          
            else:
                try:
                    item.aumentar_estoque(quantidade)
                    session.commit()
                    print("Estoque atualizado com sucesso!")

                except ValueError as e:
                    session.rollback()
                    print("Erro ao atualizar o estoque:", str(e))
            
        elif opcao == 4:
            while True:
                try:
                    id_item = int(input("ID do item: "))
                    quantidade = int(input("Quantidade: "))
                    break
                except ValueError:
                    print("Digite somente números inteiros!")
                    continue

            item = session.query(Item).filter_by(id=id_item).first()
            if item is None:
                print("Item não encontrado.")
                sleep(1)

            else:
                try:
                    item.diminuir_estoque(quantidade)
                    session.commit()
                    print("Estoque atualizado com sucesso!")

                except ValueError as e:
                    session.rollback()
                    print("Erro ao atualizar o estoque:", str(e))
                    

                except SQLAlchemyError as i:
                    session.rollback()
                    print("Erro ao atualizar o estoque:", str(i))

        elif opcao == 5:

            while True:
                try:
                    id_item = int(input("ID do Item a ser excluido: "))
                    break
                except ValueError:
                    print("Digite somente números inteiros!")
                    continue
            item = session.query(Item).filter_by(id=id_item).first()
            
            if item is None:
                print(f"Item com ID: {id_item} não foi encontrado")

            else:
                try:
                    session.delete(item)
                    session.commit()
                    print("Produto exluido com sucesso!")
                    

                except SQLAlchemyError as e:
                    session.rollback()
                    print("Erro ao excluir item do estoque!", str(e))


        elif opcao == 6:
            print("Saindo do programa...")
            sleep(1)
            break
            


def cadastrar_item():
    while True:
        categoria = input("Categoria: ").strip()
        if not categoria:
            print("Erro: Categoria não deve ter campo vazio.")
            continue

        nome = input("Nome: ").strip()
        if not nome:
            print("Erro: O nome não deve ter campo vazio.")
            continue

        
        categoria = categoria.upper()
        nome = nome.upper()            
        
        
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade invalida, Digite um número positivo.")
                continue

        except ValueError:
            print("ERRO: Digite apenas números inteiros.")
            continue

        try:
            novo_item = Item(categoria=categoria, nome=nome, quantidade=quantidade)
            session.add(novo_item)
            session.commit()
            print(f"{novo_item.nome} cadastrado com sucesso com: {novo_item.quantidade} Qnt.")
            if categoria == 'HARDWARE':
                novo_item = Item_hardware(categoria=categoria, nome=nome, quantidade=quantidade)
                session.add(novo_item)
                session.commit()
                break
        except SQLAlchemyError as e:
            session.rollback()
            print("Erro ao salvar o item:", e)
            break
                    

                    
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



    

    