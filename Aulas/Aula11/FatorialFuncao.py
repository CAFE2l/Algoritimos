
num = int(input("Digite um número: "))

def Fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * Fatorial(x - 1)

        

Fat = Fatorial(num)
print(f"O fatorial de {num} é {Fat}")