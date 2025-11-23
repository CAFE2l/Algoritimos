num = int(input(f"Digite um número: "))

def ParouImpar(num):
    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é ímpar")

ParouImpar(num)