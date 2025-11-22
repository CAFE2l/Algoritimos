
cont = 1
TotN = 0
num = int(input("Digite um número: "))
while cont <= 5:
    if num < 0:
        TotN += 1
    cont += 1
print(f"Foram digitados {TotN} números negativos.")