cont = 1
num = int(input("Digite um número: "))
contDiv = 0
while cont < num:
    print(cont, end=" ")
    if num % cont == 0: 
        contDiv += 1
    cont += 1
if contDiv > 2:
    print(f"\nO número {num} NÃO é primo.")
else:
    print(f"\nO número {num} É primo.")
print(f"\nAo todo existem {contDiv} valores divisíveis por {num}.")