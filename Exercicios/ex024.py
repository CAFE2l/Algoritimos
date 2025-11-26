km = float(input("Quantos Km vc vai percorrer? "))
curta = km * 0.50
longa = km * 0.45
if (km <= 200):
    print(f"sua viagem é curta vc vai pagar {curta:.2f}")
else: 
    print(f"sua viagem é longa vc vai pagar {longa:.2f}")