cont = 1
TotN = 0
while cont <= 5:
    num = int(input("Digite um número: "))
    if num < 0:
        TotN += 1
    cont += 1
print(f"Foram digitados {TotN} números negativos.")
