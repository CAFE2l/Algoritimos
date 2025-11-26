peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))
imc = peso / (altura * altura)
if (imc < 18.5):
    print(f"Abaixo do peso")
elif (imc >= 18.5 and imc < 25):
    print(f"Peso ideal")
elif (imc >= 25 and imc < 30):
    print(f"Sobrepeso")
elif (imc >= 30 and imc < 40):
    print(f"Obesidade")
else:
    print(f"Obesidade mórbida")