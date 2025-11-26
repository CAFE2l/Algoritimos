comprimento1 = float(input(f"Digite o comprimento da primeira reta: "))
comprimento2 = float(input(f"Digite o comprimento da segunda reta: "))
comprimento3 = float(input(f"Digite o comprimento da terceira reta: "))

if (comprimento1 + comprimento2 > comprimento3) and (comprimento1 + comprimento3 > comprimento2) and (comprimento2 + comprimento3 > comprimento1):
    print(f"Essas retas podem formar um triângulo")
else:
    print(f"Essas retas não podem formar um triângulo")