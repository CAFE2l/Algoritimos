import random

# Cria vetor com 30 posições preenchidas com números aleatórios entre 1 e 15
vetor = []
for i in range(30):
    vetor.append(random.randint(1, 15))

# Pede a chave para o usuário APÓS preencher o vetor
chave = int(input("Digite uma chave misteriosa (1 a 15): "))

# Lista para armazenar as posições onde a chave foi encontrada
posicoes = []
contador = 0

# Procura a chave no vetor
for i in range(30):
    if vetor[i] == chave:
        posicoes.append(i)      # Armazena a posição (índice)
        contador += 1           # Conta quantas vezes apareceu

# Exibe os resultados
print(f"Vetor gerado: {vetor}")
print(f"A chave {chave} foi encontrada nas posições: {posicoes}")
print(f"A chave {chave} apareceu {contador} vez(es)")
