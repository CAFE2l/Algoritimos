def fibonacci(n):
    a, b = 1, 1          # Inicializa os dois primeiros termos
    sequencia = []       # Lista para armazenar os termos
    for _ in range(n):
        sequencia.append(a)  # Adiciona termo atual
        a, b = b, a + b       # Atualiza os valores
    return sequencia

n = int(input("Quantos números da sequência de Fibonacci deseja mostrar? "))
resultado = fibonacci(n)
print(resultado)
