largura = float(input(f"Digite a largura do terreno: "))
comprimento = float(input(f"Digite o comprimento do terreno: "))
area = comprimento * largura 
print(f"A área do terreno é {area:.2f}m²")
if (area <= 100):
    print(f"TERRENO POPULAR")
elif (area > 100 and area <= 500):
    print("TERRENO MASTER")
else:
    print("TERRENO VIP")