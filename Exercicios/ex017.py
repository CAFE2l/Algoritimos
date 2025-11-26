velocidade = float(input(f"Qual a velocidade do carro? "))
if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"Você foi multado por R${multa:.2f}")
else:
    print(f"Ta certo patrão marcha marcha")