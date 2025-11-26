Rodados = float(input(f"Quantos KM você percorreu com o carro? "))
Dias = int(input(f"Quantos dias você ficou com o carro? "))
Total = (Dias * 90) + (Rodados * 0.20)
print(f"Voê terá que pagar R${Total:.2f}")