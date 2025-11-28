def contador():
    inicio = int(input("Digite o valor inicial: "))
    fim = int(input("Digite o valor final: "))
    passo = int(input("Digite o passo: "))

    for i in range(inicio, fim+1, passo):
        print(i, end=" ")

contador()