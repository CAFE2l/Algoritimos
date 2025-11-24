# Cria uma matriz 3x2 (3 linhas, 2 colunas) inicializada vazia
matriz = []
numerosPares = []
numerosImpares = []
# Preenche a matriz com valores digitados pelo usuário
for L in range(0, 3):
    linha = []  # Cria uma nova linha vazia
    for c in range(0, 3):
        valor = int(input(f"Digite o valor da posição [{L},{c}]: ")) # Lê o valor
        if valor % 2 == 0:
            numerosPares.append(valor)
        else: 
            numerosImpares.append(valor)
        linha.append(valor)  # Adiciona o valor na linha
    matriz.append(linha)     # Adiciona a linha completa na matriz

# Exibe os valores da matriz formatados
for L in range(0, 3):
    for c in range(0, 3):
        print(f"{matriz[L][c]:4}", end=" ")  # Mostra cada elemento da linha
    print()  # Pula para a próxima linha

print(f"Os valores pares foram: {numerosPares}")
print(f"Os valores impares foram: {numerosImpares}")

#Solução do guaná:'

# matriz = []


        