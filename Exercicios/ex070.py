# Função para gerar a sequência de Fibonacci com n termos
def fibonacci(n):
    a, b = 0, 1          # Inicializa os dois primeiros termos
    sequencia = []       # Lista para armazenar os termos
    for _ in range(n):
        sequencia.append(a)  # Adiciona o termo atual na lista
        a, b = b, a + b      # Atualiza os valores de a e b (a se torna b, b se torna soma dos dois)
    return sequencia

# Número de termos que desejamos na sequência
n = 10

# Gera e imprime a sequência
resultado = fibonacci(n)
print("Sequência de Fibonacci:")
print(resultado)
