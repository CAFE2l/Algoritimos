numerosPares = 0
numerosImpares = 0
for i in range(0, 6):
    num = int(input(f"Digite o {i+1} número: "))
    if (num % 2 == 0):
        numerosPares += 1
     
    else:
        numerosImpares += 1
      

print("acabou")
print(f"Os números pares foram {numerosPares}")
print(f"Os números impares foram {numerosImpares}")