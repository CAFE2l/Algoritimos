horas = int(input("Quantas horas de atividade vc teve no mês? "))

# Inicializa pontos com 0
pontos = 0

if horas <= 10:
    pontos = 2 * horas
    print("Ganhou 2 pontos por hora")
elif horas <= 20:
    pontos = 5 * horas
    print("Ganhou 5 pontos por hora")
else:
    pontos = 10 * horas
    print("Ganhou 10 pontos por hora")

reais = pontos * 0.05

print(f"Pontos ganhos: {pontos} e R${reais:.2f}")
