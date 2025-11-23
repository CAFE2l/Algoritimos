Num = int(input("Digite um número: "))

def ParOuImpar(num):
    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é ímpar")

ParOuImpar(Num)