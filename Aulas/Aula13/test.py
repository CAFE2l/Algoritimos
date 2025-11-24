# 1. Começa com uma lista vazia, que será a nossa "matriz"
matriz = []

# 2. Loop de Fora (para as LINHAS)
#    Este loop vai rodar 3 vezes (para a linha 0, linha 1, linha 2)
print("Digite os valores para a matriz 3x3:")
for i in range(0, 3):
    
    # 3. Cria uma lista vazia temporária para ser a "linha"
    linha = []
    
    # 4. Loop de Dentro (para as COLUNAS)
    #    Este loop vai rodar 3 vezes para CADA linha
    #    (para a coluna 0, coluna 1, coluna 2)
    for j in range(0, 3):
        
        # 5. Pede ao usuário um valor e o guarda na variável 'valor'
        #    O f-string mostra a coordenada (ex: "Linha 0, Coluna 1")
        #    O int() transforma o texto digitado em número
        valor = int(input(f"Digite o valor para [Linha {i}][Coluna {j}]: "))
        
        # 6. Adiciona (append) o valor na lista 'linha'
        linha.append(valor)
        
    # 7. Quando o loop de DENTRO (colunas) termina, a 'linha' está pronta.
    #    Adicionamos (append) a 'linha' inteira na 'matriz'.
    matriz.append(linha)


# --- BÔNUS: Como Exibir a Matriz de forma bonita ---

print("\nSua matriz 3x3 é:")
# Loop para passar por cada 'linha' dentro da 'matriz'
for linha in matriz:
    # Imprime a lista 'linha' inteira (que é [val1, val2, val3])
    print(linha)

# Exemplo de como acessar um item (Linha 1, Coluna 1)
print(f"\nO valor no centro da matriz [1][1] é: {matriz[1][1]}")