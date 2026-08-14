from models import Item, ItemHardware, ItemPeriferico, ItemComputador,ItemProjetor,ItemAcessorio, session
from time import sleep
from sqlalchemy.exc import SQLAlchemyError

lista_status = ['LIXO', 'FUNCIONANDO', 'CONSERTO']
lista_categorias = ['PERIFERICO', 'DESKTOP', 'NOTEBOOK', 'HARDWARE', 'PROJETOR', 'ACESSORIO']




def menu():
    while True:
        try:
            print("\nEstoque T.I UniEnsino")
            print("1 - Cadastrar um novo item ")
            print("2 - Listar itens")
            print("3 - Aumentar estoque")
            print("4 - Diminuir estoque")
            print("5 - Apagar item do estoque")
            print("6 - Lixeira")
            print("7 - Sair")
            opcao = int(input("Escolha uma opcao: "))
            if 1 <= opcao <= 7:
                return opcao
            else:
                print("Opção invalida. Escolha um número entre 1 e 7.")
        except ValueError:
            print("Entrada inválida. Digite o número da opção.")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Saindo.")
            return 7



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

                except SQLAlchemyError as i:
                    session.rollback()
                    print("Erro ao atualizar o estoque:", str(i))
            
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
            item_lixo = session.query(Item).filter_by(status='LIXO').all()
            if not item_lixo:
                print("Nenhum item encontrado na lixeira!")
            else:
                print("\n --- ITENS NA LIXEIRA ---")
                for lixo in item_lixo:
                    print(f"ID: {lixo.id} | Nome: {lixo.nome}| Categoria: {lixo.categoria} | Quantidade: {lixo.quantidade} | Status: {lixo.status}")
                    print("-" * 20)

        elif opcao == 7:
            print("Saindo do programa...")
            sleep(1)
            break
            


def cadastrar_item():
    while True:
        print("\n--- LISTA DE CATEGORIAS ---")
        print("PERIFERICO | DESKTOP | NOTEBOOK | HARDWARE | PROJETOR | ACESSORIO")
        categoria = input("Categoria: ").strip().upper()
        if not categoria:
            print("Erro: Categoria não deve ter campo vazio.")
            continue
        if categoria not in lista_categorias:
            print("Erro: Categoria deve ser uma das opções validas!")
            continue

        nome = input("Nome: ").strip().upper()
        if not nome:
            print("Erro: O nome não deve ter campo vazio.")
            continue

        status = str(input("Status do item (Lixo | Funcionando | Conserto): ")).strip().upper()
        if not status:
            print("Erro: Status não deve ter campo Vazio.")
            continue
        if status not in lista_status:
            print("Erro: Status deve estar entre as 3 opções indicadas!")
            continue
                
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade invalida, Digite um número positivo.")
                continue

        except ValueError:
            print("ERRO: Digite apenas números inteiros.")
            continue

        setor = None
        responsavel = None
        if categoria == 'DESKTOP' or categoria == 'NOTEBOOK':
            setor = input("Setor: ").strip().upper()
            if not setor:
                print("Setor não pode ser um campo vazio.")
                continue  
            responsavel = input("Usuario responsável (deixe em branco se for do T.I): ").strip().upper()
            if not responsavel:
                responsavel = 'T.I'
        elif categoria == 'PROJETOR':
            modelo = input("Modelo: ").strip().upper()
            if not modelo:
                print("Modelo não pode ser um campo vazio.")
                continue
        try:
            novo_item = Item(categoria=categoria, nome=nome, quantidade=quantidade, status=status)
            session.add(novo_item)
            session.commit()
            print(f"{novo_item.nome} cadastrado com sucesso com: {novo_item.quantidade} Unidade.")
            if categoria == 'HARDWARE':
                session.add(ItemHardware(item_id=novo_item.id))
                session.commit()

            elif categoria == 'PERIFERICO':
                session.add(ItemPeriferico(item_id=novo_item.id))
                session.commit()

            elif categoria == 'DESKTOP' or categoria == 'NOTEBOOK':
                session.add(ItemComputador(item_id=novo_item.id, setor=setor, responsavel=responsavel))
                session.commit()

            elif categoria == 'PROJETOR':
                session.add(ItemProjetor(item_id=novo_item.id, modelo=modelo))
                session.commit()

            elif categoria == 'ACESSORIO':
                session.add(ItemAcessorio(item_id=novo_item.id))
                session.commit()
            break

        except SQLAlchemyError as e:
            session.rollback()
            print("Erro ao salvar o item:", e)
            break

def listar_itens():
    categorias = [c[0] for c in session.query(Item.categoria).distinct().all()]

    print("\nSelecione a categoria")
    print("0 - Todos")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} - {cat}")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                itens = session.query(Item).all()
            elif opcao < 0 or opcao > len(categorias):
                print("Erro: Digite uma opcao valida!")
                continue
            else:
                categoria_escolhida = categorias[opcao - 1]
                itens = session.query(Item).filter_by(categoria=categoria_escolhida).all()

            if not itens:
                print("Nenhum Item encontrado.")
                return
            else:
                print("\n --- Itens no Estoque ---")
                for item in itens:
                    print(f"ID: {item.id} | Categoria:{item.categoria} | Nome: {item.nome} | Quantidade: {item.quantidade} | Status: {item.status} | Data: {item.data.strftime('%d/%m/%Y %H:%M:%S')}")
        except ValueError:
            print("Erro: Entrada invalida! Digite o numero da opção.")
            continue

        break



if __name__ == "__main__":
    try:
        menu_principal()
    finally:
        session.close()
        print("Sessão finalizada com segurança.")



    

    