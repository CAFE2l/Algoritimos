# QuantosEntre0e10.py
Tot010 = 0
Simp = 0
for c in range(1, 6):
    valor = int(input("Digite um valor: "))
    if valor >= 0 and valor <= 10:
        Tot010 += 1
        if valor%2 == 1:
            Simp += valor
print(f"Ao todo forma {Tot010} valores entre 0 e 10.")
print(f"A soma dos valores ímpares entre 0 e 10 é {Simp}.")