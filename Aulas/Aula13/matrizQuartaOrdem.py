cores = {
    "limpa": "\033[m",
    'vermelho': "\033[31m",
    'verde': "\033[32m",
    'amarelo': "\033[33m",
    'azul': "\033[34m",
    'roxo': "\033[35m",
    'ciano': "\033[36m",
    'cinza': "\033[37m",
    'pretoebranco': '\033[7;30m'
}

fundo = {
    "branco": "\033[40m",
    'vermelho': "\033[41m",
    'verde': "\033[42m",
    'amarelo': "\033[43m",
    'azul': "\033[44m",
    'roxo': "\033[45m",
    'ciano': "\033[46m",
    'cinza': "\033[47m",
    'vermelho_claro': '\033[101m',
    'verde_claro': '\033[102m',
    'amarelo_claro': '\033[103m',
    'azul_claro': '\033[104m',
    'roxo_claro': '\033[105m',
    'ciano_claro': '\033[106m',
    'cinza_claro': '\033[107m'
}

estilos = {
    "reset": "\033[0m",
    "negrito": "\033[1m",
    "fraco": "\033[2m",
    "italico": "\033[3m",
    "sublinhado": "\033[4m",
    "inverso": "\033[7m",
    "invisivel": "\033[8m",
    "tachado": "\033[9m",
    "duplosublinhado": "\033[21m",
    "normal": "\033[22m",
    "semitalico": "\033[23m",
    "sem_sublinhado": "\033[24m",
    "sem_inverso": "\033[27m",
    "visivel": "\033[28m",
    "sem_tachado": "\033[29m"
}

frase = "MALDITA MATRIZ 4X4"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}MATRIZ4X4{cores['verde']}{"==="*4}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

# 1. Define a ordem da matriz (4x4)
ordem = 4

# 2. Inicia a matriz (a lista principal) vazia
matriz = []
somaDiagonalPrincipal = 0
produto2Linha = 1
mai3C = 0 # Você não usou, mas vou inicializar para o cálculo bônus

print(f"{cores['cinza']}{estilos['negrito']}--- Preenchendo a Matriz de Ordem {ordem} ---")

# 3. Loop de Fora (Controla as LINHAS)
for i in range(0, ordem):
    
    # 4. A cada nova linha, cria uma lista vazia para ela
    linha_atual = []
    
    # 5. Loop de Dentro (Controla as COLUNAS)
    for j in range(0, ordem):
        
        # 6. Pede o valor para a coordenada [i][j]
        valor = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o valor para {cores['azul']}{estilos['italico']}[Linha {i}][Coluna {j}]:{cores['limpa']} "))
        
        # 7. Adiciona (append) o valor na LINHA ATUAL
        linha_atual.append(valor)

        # 8. Cálculo da Soma da Diagonal Principal (ESTÁ CORRETO AQUI)
        if (i == j):
            somaDiagonalPrincipal += valor

        # !! O CÁLCULO DO PRODUTO FOI REMOVIDO DAQUI !!
        
    # 9. Adiciona (append) a LINHA inteira na MATRIZ principal.
    matriz.append(linha_atual)


# --- Mostrando o resultado ---
print(f"\n{cores['amarelo']}{estilos['negrito']}--- Matriz {ordem}x{ordem} Completa ---{estilos['reset']}")
for linha in matriz:
    print(linha)
    
print(f"{cores['cinza']}{estilos['negrito']}A soma da diagonal principal é: {cores['verde']}{estilos['italico']}{somaDiagonalPrincipal}{cores['limpa']}")


# --- CÁLCULOS FEITOS DEPOIS DA MATRIZ ESTAR PRONTA (O LUGAR CORRETO) ---

# 1. Cálculo do Produto da 2ª Linha (ÍNDICE 1)
indice_da_linha = 1 # A "segunda linha" é a de índice 1
for j in range(0, ordem):
    # Correção: acessa a matriz[linha][coluna] e usa a atribuição *=
    produto2Linha *= matriz[indice_da_linha][j]

print(f"{cores['cinza']}{estilos['negrito']}O produto dos valores da segunda linha {cores['vermelho']}(linha 1){cores['cinza']} é: {cores['verde']}{produto2Linha}{cores['limpa']}")


# 2. (Bônus) Cálculo do Maior Valor da 3ª Coluna (ÍNDICE 2)
#    (Já que você criou a variável 'mai3C')
indice_da_coluna = 2 # A "terceira coluna" é a de índice 2

# Inicializa 'mai3C' com o primeiro valor da coluna (matriz[0][2])
mai3C = matriz[0][indice_da_coluna] 

# Loop pelas LINHAS (i), olhando sempre a mesma COLUNA
for i in range(1, ordem): # Começa do 1, pois já pegamos o 0
    if matriz[i][indice_da_coluna] > mai3C:
        mai3C = matriz[i][indice_da_coluna]

print(f"{cores['cinza']}{estilos['negrito']}O maior valor da terceira coluna {cores['amarelo']}(coluna 2) {cores['cinza']}é: {cores['azul']}{mai3C}")