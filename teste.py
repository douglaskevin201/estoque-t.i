while True:
    try:
        print("\nSelecione a categoria")
        print("1 - Todos")
        print("2 - Hardware")
        opcao = int(input("Escolha uma opção: "))
        if 1 <= opcao <= 2:
            return opcao
        else:
            print("Opcao invalida digite um numero entre 1 e 2!")
    except ValueError:
                print("Entrada inválida. Digite o número da opção.")