comprimento1 = float(input(f"Digite o comprimento da primeira reta: "))
comprimento2 = float(input(f"Digite o comprimento da segunda reta: "))
comprimento3 = float(input(f"Digite o comprimento da terceira reta: "))

if (comprimento1 + comprimento2 > comprimento3) and (comprimento1 + comprimento3 > comprimento2) and (comprimento2 + comprimento3 > comprimento1):
    print(f"Essas retas podem formar um triângulo")
else:
    print(f"Essas retas não podem formar um triângulo")

if (comprimento1 == comprimento2 and comprimento1 == comprimento3 and comprimento2 == comprimento3):
    print(f"O triangulo é EQUILATERO pois todos os lados são iguais")
elif (comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3):
    print(f"O triangulo é ISÓSCELES pois dois lados são iguais")
else:
    print(f"O triangulo é ESCALENO pois todos os lados são diferentes")