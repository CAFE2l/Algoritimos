def ParOuImpar():
    num = int(input("Digite um número: "))

    if (num % 2 == 0):
        return print(f"O número {num} é par")
    else:
        return print(f"O número {num} é impar")


ParOuImpar()