valor = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
if (valor > valor2):
    print(f"O valor {valor} é maior que o {valor2}")
elif (valor2 > valor):
    print(f"O valor {valor2} é maior que o {valor}")
else:
    print(f"Não existe valor maior, os dois são iguais")