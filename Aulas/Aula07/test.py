cont = 1
soma = 0
maior = 0
menor = 0 
while cont <= 10: 
    num = int(input(f"Digite o {cont}º número: "))
    if num > maior:
        maior = num
    if num < menor: 
        menor = num       
    soma += num
    cont += 1
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
print("A soma dos números é:", soma)