frase = str(input("Digite um frase qualquer: "))

def borda():
    escolha = int(input("Escolha uma borda para decorar sua frase(1 ou 2 ou 3): "))
    if (escolha == 1):
        print("+-----==============-----+")
        print(frase)
        print("+-----==============-----+")
    elif (escolha == 2):
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(frase)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
    elif (escolha == 3):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(frase)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

borda()