# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print(f"\nOs 10 primeiros termos da PA são:")
soma = 0

# Loop para mostrar os 10 primeiros termos e acumular a soma
for i in range(10):
    termo = primeiro_termo + (i * razao)
    print(f"Termo {i+1}: {termo}")
    soma += termo

# Exibe a soma total dos 10 termos
print(f"\nSoma dos 10 primeiros termos: {soma}")
