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

frase = "JOGO DA veIA"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}veIA{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 


def criar_tabuleiro():

    # Esta é a nossa matriz! Uma lista que contém 3 listas (as linhas)
    tabuleiro = [
        [" ", " ", " "],  # Linha 0
        [" ", " ", " "],  # Linha 1
        [" ", " ", " "]   # Linha 2
    ]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
  
    print(f"\n   {cores['amarelo']}{estilos['negrito']}--- JOGO DA VELHA ---")
    print(f"     0   1   2  <-- Colunas")
    for i in range(3):
        # Imprime a linha 0, 1 ou 2, e depois a 'linha' da matriz
        print(f"{cores['cinza']}{estilos['negrito']} {i}   " + " | ".join(tabuleiro[i]))
        if i < 2:
            # Imprime uma linha divisória
            print(f"    {cores['cinza']}{estilos['negrito']}---+---+---{cores['limpa']}")
    print(f" (Linhas)")


# --- 2. FUNÇÕES DE VERIFICAÇÃO ---

def verificar_jogada(tabuleiro, linha, coluna):

    
    # Verifica se os números estão dentro do tabuleiro (0, 1 ou 2)
    if not (0 <= linha <= 2 and 0 <= coluna <= 2):
        print(f"{cores['vermelho']}{estilos['negrito']}Erro: Posição fora do tabuleiro. Use números de 0 a 2.{cores['limpa']}")
        return False
    
    # Verifica se a célula da matriz [linha][coluna] está vazia (" ")
    if tabuleiro[linha][coluna] != " ":
        print(f"{cores['vermelho']}{estilos['negrito']}Erro: Posição já ocupada. Escolha outra.{cores['limpa']}")
        return False
    
    # Se passou nas duas verificações, a jogada é válida
    return True

def verificar_vencedor(tabuleiro, jogador):

    # Verificar Linhas Horizontais
    for i in range(3):
        if (tabuleiro[i][0] == jogador and 
            tabuleiro[i][1] == jogador and 
            tabuleiro[i][2] == jogador):
            return True
            
    # Verificar Colunas Verticais
    for j in range(3):
        if (tabuleiro[0][j] == jogador and 
            tabuleiro[1][j] == jogador and 
            tabuleiro[2][j] == jogador):
            return True
            
    # Verificar Diagonais
    # Diagonal 1 (Topo-Esquerda para Baixo-Direita)
    if (tabuleiro[0][0] == jogador and 
        tabuleiro[1][1] == jogador and 
        tabuleiro[2][2] == jogador):
        return True
        
    # Diagonal 2 (Topo-Direita para Baixo-Esquerda)
    if (tabuleiro[0][2] == jogador and 
        tabuleiro[1][1] == jogador and 
        tabuleiro[2][0] == jogador):
        return True
        
    # Se nenhuma condição de vitória foi atingida
    return False

def verificar_velha(tabuleiro):

    # Se acharmos QUALQUER espaço vazio " ", o jogo não deu velha
    for linha in tabuleiro:
        for celula in linha:
            if celula == " ":
                return False
                
    # Se o loop terminar e não achar espaços vazios, deu velha
    return True

# --- 3. LOOP PRINCIPAL DO JOGO ---

def jogar_jogo():

    
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X" # O 'X' sempre começa
    
    # Loop principal do jogo
    while True:
        # 1. Mostra o tabuleiro atual
        imprimir_tabuleiro(tabuleiro)
        
        # 2. Pede a jogada ao usuário
        print(f"\nÉ a vez do Jogador: '{jogador_atual}'")
        
        try:
            linha = int(input(f"{cores['cinza']}{estilos['negrito']}Digite a LINHA {cores['ciano']}{estilos['italico']}(0, 1 ou 2): "))
            coluna = int(input(f"{cores['cinza']}{estilos['negrito']}Digite a COLUNA {cores['ciano']}{estilos['italico']}(0, 1 ou 2): "))
        except ValueError:
            # Se o usuário não digitar um NÚMERO
            print(f"{cores['vermelho']}{estilos['negrito']}Erro: Entrada inválida. Por favor, digite apenas números.{cores['limpa']}")
            continue # Pula de volta para o início do loop

        # 3. Verifica se a jogada é válida
        if not verificar_jogada(tabuleiro, linha, coluna):
            continue # Pede uma nova jogada

        # 4. Se a jogada for válida, marca na matriz
        tabuleiro[linha][coluna] = jogador_atual
        
        # 5. Verifica se o jogador atual venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"\n{cores['verde']}{estilos['negrito']}*** PARABÉNS! O JOGADOR '{jogador_atual}' VENCEU! ***{cores['limpa']}")
            break # Encerra o jogo

        # 6. Verifica se deu velha
        if verificar_velha(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print(f"\n{cores['amarelo']}{estilos['negrito']}*** DEU VELHA! Ninguém venceu. ***{cores['limpa']}")
            break # Encerra o jogo

        # 7. Se ninguém venceu e não deu velha, troca o jogador
        if jogador_atual == "X":
            jogador_atual = "O"
        else:
            jogador_atual = "X"

# --- Executa o jogo ---
if __name__ == "__main__":
    jogar_jogo()