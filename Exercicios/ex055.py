import random 

for i in range(4):
    num = int(input("tente adivinhar um número entre 1 e 5: "))
    computador = random.randint(1, 5)

    if (num == computador):
        print("Parabéns vc acertou!!!")
        break
    else:
        print("ERROU, tente novamente")