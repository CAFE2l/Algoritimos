vet = []          # Cria lista vazia para armazenar os valores
aux = 0
for i in range(0, 10):
    valor = int(input("Digite um valor: "))   # Lê valor do usuário
    vet.append(valor)                         # Adiciona valor à lista

# Algoritmo de ordenação simples (bubble sort)
for i in range(0, 9):
    for j in range(i+1, 10):
        if vet[i] > vet[j]:                  # Se valor da posição i for maior, troca
            aux = vet[i]
            vet[i] = vet[j]
            vet[j] = aux

# Mostra os valores ordenados
for i in range(0, 10):
    print(vet[i], end=" ")


#ARREGUEI PAREI NO MINUTO 36:51 