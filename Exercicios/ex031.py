import random

# Pergunta ao usuário se quer jogar e converte resposta para maiúscula
jogar = input("Quer jogar jokenpô? [S/N] ").upper()

if jogar == "S":
    # Mostra as opções para o usuário escolher
    print("[1] Pedra\n[2] Papel\n[3] Tesoura")
    jogador = int(input("Escolha uma opção (1, 2 ou 3): "))
    
    # Verifica escolha do jogador
    if jogador == 1:
        print("Você escolheu PEDRA")
    elif jogador == 2:
        print("Você escolheu PAPEL")
    elif jogador == 3:
        print("Você escolheu TESOURA")
    else:
        print("Opção inválida!")
        exit()  # Encerra o programa se opção errada

    # Computador escolhe aleatoriamente entre 1, 2 e 3
    computador = random.randint(1, 3)
    if computador == 1:
        print("Computador escolheu PEDRA")
    elif computador == 2:
        print("Computador escolheu PAPEL")
    else:
        print("Computador escolheu TESOURA")

    # Define as regras do jogo para decidir o vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        print("Você ganhou!")
    else:
        print("Computador ganhou!")

else:
    print("Jogo encerrado. Até a próxima!")
