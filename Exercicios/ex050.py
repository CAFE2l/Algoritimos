import random
maior5 = 0
divisiveis3 = 0
sorteio = random.randint(0,10)
for sorteio in range(0, 20):
    if (sorteio % 3 == 0):
        divisiveis3 += 1
    elif (sorteio > 5):
        maior5 += 1
print(f"Os números sorteados foram: {sorteio}")
print(f"Os números divisiveis por 3 foram: {divisiveis3}")
print(f"Os números acima de 5 foram: {maior5}")