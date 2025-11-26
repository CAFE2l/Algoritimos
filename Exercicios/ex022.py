nascimento = int(input(f"Em que ano você nasceu? "))
idade = 2025 - nascimento
if (idade > 18):
    anos = idade - 18
    print(f"Você devia ter se alistado a {anos} anos atras")
elif (idade == 18):
    print(f"Você deve se alistar esse ano")
else:
    anos = 18 - idade
    print(f"Ainda faltam {abs(anos)} anos para você se alistar")