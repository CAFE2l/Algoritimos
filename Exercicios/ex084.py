
# 1. CRIANDO AS DUAS LISTAS (VETORES) VAZIAS
nomes = []      # Lista para armazenar todos os nomes das 9 pessoas
idades = []     # Lista para armazenar todas as idades das 9 pessoas
                # IMPORTANTE: Mesma posição = mesma pessoa (índice 0=1ªpessoa)

# 2. LOOP PARA LER EXATAMENTE 9 PESSOAS
for i in range(9):  # range(9) gera números 0,1,2,3,4,5,6,7,8 (9 iterações)
    # Solicita o nome da pessoa atual (i+1 para mostrar 1,2,3... ao invés de 0,1,2...)
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    
    # Solicita a idade e converte para inteiro (int)
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    
    # ADICIONA na MESMA POSIÇÃO dos dois vetores (relação mantida)
    nomes.append(nome)   # append adiciona no final da lista
    idades.append(idade)



menores_encontrados = False    # Flag (bandeira) para verificar se achou alguém

# 4. LOOP PARA PERCORRER E FILTRAR MENORES
for i in range(9):             # Percorre as mesmas 9 posições
    if idades[i] < 18:         # CONDIÇÃO: idade menor que 18
        # MOSTRA nome e idade da posição i (mesma pessoa)
        print(f"Nome: {nomes[i]} - Idade: {idades[i]} anos")
        menores_encontrados = True  # Achou menor, marca como True

# 5. CASO NÃO ACHE NENHUM MENOR
if not menores_encontrados:
    print("Nenhuma pessoa menor de idade encontrada.")
