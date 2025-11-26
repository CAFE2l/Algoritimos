compras = 1320
sexo = str(input("Qual seu sexo? [M/F]")).upper()
if (sexo == "F"):
    print(f"Mulheres ganham 13% de desconto")
    desconto = compras * 0.13
    print(f"O valor da sua compra deu {compras - desconto:.2f}")
elif (sexo == "M"):
    print(f"Homens ganham 5% de desconto")
    desconto = compras * 0.05
    print(f"O valor da sua compra deu {compras - desconto:.2f}")
else:
    print(f"Sexo inválido")