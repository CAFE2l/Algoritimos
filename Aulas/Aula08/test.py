soma = 0 
resp = 'S'
while resp == 'S': 
    num = int(input(f"Digite o valor ==> "))
    soma = soma + num
    resp = str(input("Quer continuar? [S/N] ")).upper()

print("A soma dos valores é igual a ", soma)