while True:
    num = int(input(f"Digite um número para calcular o fatorial: "))
    fatorial = 1 
    cont = num 
    while cont > 0:
        print(f"{cont}", end="")
        print(" x " if cont > 1 else " = ", end="")
        fatorial *= cont
        cont -= 1
    print(f"{fatorial}")
    R = str(input("Quer continuar? [S/N] "))
    if R != "S" and R !="s":
        break