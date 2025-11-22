cont = 1
Quant = int(input("Quantas conversões você deseja fazer? "))
while cont <= Quant:
    real = float(input(f"Qual o valor em R$ "))
    dolar = real / 5.25
    print("O valor convertido em dólar é: U$ {:.2f}".format(dolar))
    cont += 1