
aluguel = str(input("Qual carro deseja alugar? [P/L]")).upper()
km = float(input("Quantos km vc percorreu? "))
dias = int(input("Quantos dias vc ficou com o carro? "))
if (aluguel == "P"):
    if (km <= 100):
        preço = 90 * dias + (0.20 * km)
    else:
        preço = 90 * dias + (0.10 * km)

    total = preço
    print(f"O total a pagar é R${preço:.2f}")
else: 
    if (km <= 200):
        preço = 150 * dias + (0.30 * km)
    else:
        preço = 150 * dias + (0.25 * km)

    total = preço
    print(f"O total a pagar é R${preço:.2f}")