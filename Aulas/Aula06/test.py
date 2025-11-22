opcao = input("Escolha uma opção (1,2 ou 3): ")

match opcao: 
    case "1":
        print("Você escolheu a opção 1")
    case "2":
        print("Você escolheu a opção 2")
    case "3":
        print("Você escolheu a opção 3")
    case _:
        print("Opção inválida")