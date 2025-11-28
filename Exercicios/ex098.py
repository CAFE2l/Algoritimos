def super_somador(inicio, fim):
    """
    Recebe 2 parâmetros e retorna a soma de todos os valores
    no intervalo [inicio, fim] (inclusive)
    """
    soma = 0  # Acumulador da soma
    
    for numero in range(inicio, fim + 1):  # +1 para incluir o 'fim'
        soma += numero  # Adiciona cada número à soma total
    
    return soma  # Retorna o resultado da soma

# Uso da função
resultado = super_somador(1, 5)
print(f"Soma de 1 até 5: {resultado}")  # Saída: 15 (1+2+3+4+5)
