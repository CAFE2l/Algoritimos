
a, b = 1, 1          # Inicializa os dois primeiros termos
sequencia = []       # Lista para armazenar os termos
for _ in range(0, 16):
    sequencia.append(a)  # Adiciona o termo atual na lista
    a, b = b, a + b      # Atualiza os valores de a e b (a se torna b, b se torna soma dos dois)



# Gera e imprime a sequência
print("Sequência de Fibonacci:")
print(sequencia)
