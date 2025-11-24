# 1. Começa com a matriz vazia (a lista de fora)
mID = []

# 2. Loop de Fora (Controla as LINHAS)
for i in range(0, 3):
    
    # 3. CRIA UMA NOVA LISTA VAZIA PARA SER A LINHA
    #    Isso é o mais importante! A cada nova linha (i), 
    #    nós criamos uma "prateleira" nova.
    linha_atual = []
    
    # 4. Loop de Dentro (Controla as COLUNAS)
    for j in range(0, 3):
        
        # 5. A SUA LÓGICA (Está correta!)
        #    Se a linha (i) for igual à coluna (j)...
        if (i == j):
            # 6. Adiciona 1 na LINHA ATUAL
            linha_atual.append(1)
        else:
            # 7. Senão, adiciona 0 na LINHA ATUAL
            linha_atual.append(0)
            
    # 8. FIM DO LOOP DAS COLUNAS
    #    A linha_atual agora está pronta (ex: [1, 0, 0])
    #    Adiciona (append) a LINHA INTEIRA na matriz principal 'mID'
    mID.append(linha_atual)

# --- FIM DE TUDO ---
print("Matriz criada com sucesso:")

# Para imprimir a matriz de forma bonita (uma linha embaixo da outra)
for linha in mID:
    print(linha)