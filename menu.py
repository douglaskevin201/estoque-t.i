from models import Item, ItemHardware, ItemPeriferico, ItemComputador,ItemProjetor,ItemAcessorio, session
from time import sleep
from sqlalchemy.exc import SQLAlchemyError

lista_status = ['LIXO', 'FUNCIONANDO', 'CONSERTO']
lista_categorias = ['PERIFERICO', 'DESKTOP', 'NOTEBOOK', 'HARDWARE', 'PROJETOR', 'ACESSORIO']




def menu():

    """Exibe o menu principal e lê a opção escolhida pelo usuário.

    Repete a leitura até receber um número válido entre 1 e 7.

    Returns:
        int: a opção escolhida (1 a 7). Retorna 7 (Sair) também em
            caso de interrupção pelo teclado (Ctrl+C).

    Raises:
        ValueError: tratado internamente — não propaga para quem
        chama a função.
    """

    while True:
        try:
            print("\nEstoque T.I UniEnsino")
            print("1 - Cadastrar um novo item ")
            print("2 - Listar itens")
            print("3 - Aumentar estoque")
            print("4 - Diminuir estoque")
            print("5 - Enviar item para lixeira")
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

    """Loop principal do programa.

    Exibe o menu, lê a opção escolhida via menu() e direciona para
    a função ou bloco correspondente (cadastro, listagem, ajuste de
    estoque, exclusão, lixeira). Roda indefinidamente até a opção
    de sair ser escolhida. 
    """

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
                    id_item = int(input("ID do Item a ser movido para lixeira: "))
                    break
                except ValueError:
                    print("Digite somente números inteiros!")
                    continue
            item = session.query(Item).filter_by(id=id_item).first()
            
            if item is None:
                print(f"Item com ID: {id_item} não foi encontrado")

            else:
                try:
                    item.status = 'LIXO'
                    session.commit()
                    print("Item movido para lixeira com sucesso!")
                    

                except SQLAlchemyError as e:
                    session.rollback()
                    print("Erro ao enviar item para lixeira!", str(e))

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

    """ Cadastra novo item no estoque.
    
        Coleta categoria, nome, status e quantidade via input do usuário,
        validando cada campo. Dependendo da categoria escolhida, também
        coleta campos extras (setor/resposável para Desktop/Notebook,
        modelo para Projetor) e associa a subclasse correspondente ao 
        Item antes de persistir tudo numa única transação.

        Raises:
            SQLAlchemyError: se ocorrer erro ao salvar no banco; a
                transação é revertida com rollback.
        """

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

            if categoria == 'HARDWARE':
                novo_item.hardware = ItemHardware()

            elif categoria == 'PERIFERICO':
                novo_item.periferico = ItemPeriferico()

            elif categoria == 'DESKTOP' or categoria == 'NOTEBOOK':
                novo_item.computador = ItemComputador(setor=setor, responsavel=responsavel)

            elif categoria == 'PROJETOR':
                novo_item.projetor = ItemProjetor(modelo=modelo)

            elif categoria == 'ACESSORIO':
                novo_item.acessorio = ItemAcessorio()
   
            session.add(novo_item)
            session.commit() 
            print(f"{novo_item.nome} cadastrado com sucesso com: {novo_item.quantidade} Unidade.")
            break

        except SQLAlchemyError as e:
            session.rollback()
            print("Erro ao salvar o item:", e)
            break

def listar_itens():

    """Lista os itens do estoque, com filtro opcional por categoria.

    As opções de categoria exibidas são construídas dinamicamente a
    partir das categorias já cadastradas no banco (via .distinct()),
    não de uma lista fixa — uma categoria só aparece como opção se
    já existir pelo menos um item cadastrado nela.

    Raises:
        ValueError: tratado internamente — não propaga para quem
        chama a função.
    """

    categorias = [
        c[0] for c in session.query(Item.categoria)
        .filter(Item.status != 'LIXO')
        .distinct()
        .all()
    ]

    print("\nSelecione a categoria")
    print("0 - Todos")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} - {cat}")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                itens = session.query(Item).filter(Item.status != 'LIXO').all()

            elif opcao < 0 or opcao > len(categorias):
                print("Erro: Digite uma opcao valida!")
                continue
            else:
                categoria_escolhida = categorias[opcao - 1]
                itens = session.query(Item).filter(
                    Item.categoria == categoria_escolhida,
                    Item.status != 'LIXO'
                ).all()

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



    

    