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

frase = "MENU DE OPCOES"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}MENU{cores['verde']}{"==="*5}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

# 1. Define a ordem da matriz (4x4)


def criar_matriz(ordem):
    matriz = []
    print(f"{estilos['negrito']}{cores['azul']}--- Preenchendo a Matriz de Ordem {ordem} ---{cores['limpa']}")
    for i in range(ordem):
        linha_atual = []
        for j in range(ordem):
            # Pede o valor para a coordenada [i][j]
            valor = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o valor para {estilos['italico']}{cores['azul']}[Linha {i}][Coluna {j}]: "))
            linha_atual.append(valor)
        matriz.append(linha_atual)
    print(f"\n{cores['verde']}{estilos['negrito']}--- Matriz criada com sucesso! ---{cores['limpa']}")
    return matriz

# --- PROGRAMA PRINCIPAL ---

# 1. Define a ordem e cria a matriz
ordem = 4
matriz = criar_matriz(ordem)

# 2. Inicia o loop infinito do menu
while True:
    # Mostra o menu de opções
    print(f"{"\n"} + {estilos['negrito']}{cores['cinza']}{"="*30}")
    print(f"      {cores['cinza']}{estilos['negrito']}   MENU DE OPÇÕES")
    print("="*30)
    print(f"{estilos['negrito']}{cores['amarelo']} 1){cores['cinza']} Mostrar a matriz completa")
    print(f"{estilos['negrito']}{cores['amarelo']} 2){cores['cinza']} Mostrar a Diagonal Principal")
    print(f"{estilos['negrito']}{cores['amarelo']} 3){cores['cinza']} Mostrar o Triângulo Superior")
    print(f"{estilos['negrito']}{cores['amarelo']} 4){cores['cinza']} Mostrar o Triângulo Inferior")
    print(f"{estilos['negrito']}{cores['amarelo']} 5){cores['cinza']} Sair")
    print("="*30)
    
    # Pede a escolha do usuário
    escolha = input(f"{estilos['negrito']}{cores['cinza']}Digite sua opção {estilos['italico']}{cores['roxo']}(1-5): {cores['limpa']}")
    # --- Opção 1: Mostrar a Matriz ---
    if escolha == '1':
        print(f"\n{cores['amarelo']}{estilos['negrito']}--- 1. Matriz Completa ---{cores['limpa']}")
        for linha in matriz:
            # Imprime cada linha da matriz
            print(linha)

    # --- Opção 2: Diagonal Principal ---
    elif escolha == '2':
        print(f"\n{cores['amarelo']}{estilos['negrito']}--- 2. Diagonal Principal ---{cores['limpa']}")
        

        elementos_diag = []
        for i in range(ordem):
            # A diagonal principal é onde o índice da linha (i)
            # é igual ao índice da coluna (j).
            # Por isso, pegamos matriz[0][0], matriz[1][1], etc.
            elementos_diag.append(matriz[i][i])
        print(elementos_diag)

    # --- Opção 3: Triângulo Superior ---
    elif escolha == '3':
        print(f"\n-{cores['amarelo']}{estilos['negrito']}-- 3. Triângulo Superior ---{cores['limpa']}")
        

        # Loop aninhado para passar por cada célula
        for i in range(ordem):
            for j in range(ordem):
                # A "mágica" está aqui:
                # Se o índice da COLUNA (j) for MAIOR ou IGUAL
                # ao índice da LINHA (i), nós mostramos o valor.
                if j >= i:
                    # O f"{valor:^4}" formata o número para ter 4 espaços
                    # e ficar alinhado. É apenas estético.
                    print(f"{estilos['negrito']}{cores['cinza']}[{matriz[i][j]:^4}]", end=" ")
                else:
                    # Se não, imprime um espaço vazio
                    print("[    ]", end=" ")
            print() # Pula para a próxima linha no final de cada 'for i'

    # --- Opção 4: Triângulo Inferior ---
    elif escolha == '4':
        print(f"\n{cores['amarelo']}{estilos['negrito']}--- 4. Triângulo Inferior ---{cores['limpa']}")
    
        for i in range(ordem):
            for j in range(ordem):
                # É a lógica oposta da anterior:
                # Se o índice da COLUNA (j) for MENOR ou IGUAL
                # ao índice da LINHA (i), nós mostramos o valor.
                if j <= i:
                    print(f"{estilos['negrito']}{cores['cinza']}[{matriz[i][j]:^4}]", end=" ")
                else:
                    print("[    ]", end=" ")
            print() # Pula para a próxima linha

    # --- Opção 5: Sair ---
    elif escolha == '5':
        print(f"\n{cores['vermelho']}{estilos['negrito']}Saindo do programa... Até logo!{cores['limpa']}")
        break # 'break' é o comando que quebra o loop 'while True' e encerra o programa

    # --- Opção Inválida ---
    else:
        print(f"\n{cores['vermelho']}{estilos['negrito']}{estilos['italico']}Opção inválida! Por favor, digite um número de 1 a 5.{cores['limpa']}")