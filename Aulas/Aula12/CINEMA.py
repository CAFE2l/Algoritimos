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

frase = "CINEMA"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}CINEMA{cores['verde']}{"==="*4+"=="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

mapa = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]

# Lista para armazenar SOMENTE as cadeiras que o usuário reservar
cadeiras_reservadas = []

# Inicia um loop infinito que só vai parar quando o usuário digitar "N"
while True: 
    
    # --- 1. DESENHA O MAPA ATUALIZADO ---
    # Este 'for' é o que você estava tentando fazer:
    print(f"\n{cores['cinza']}{estilos['negrito']}--- MAPA DAS CADEIRAS ---")
    for c in mapa:
        if c in cadeiras_reservadas:
            # Se a cadeira 'c' ESTÁ na lista de reservadas, imprime [ X ]
            print(f"{cores['cinza']}{estilos['negrito']}[ X ]", end=" ") 
        else:
            # Se a cadeira 'c' NÃO ESTÁ na lista, imprime o nome dela
            print(f"[{c}]", end=" ")
            
    print(f"\n?{cores['cinza']}{estilos['negrito']}-------------------------") # Apenas para pular a linha

    # --- 2. PERGUNTA QUAL CADEIRA RESERVAR ---
    # .upper() transforma a resposta em maiúscula (ex: 'b5' vira 'B5')
    reserva = input(f"{cores['cinza']}{estilos['negrito']}Reservar a cadeira {cores['azul']} {estilos['italico']}(ex: B5): ").upper()

    # --- 3. VALIDAÇÃO (Verifica se o usuário digitou certo) ---
    
    # 3.1 - A cadeira existe no mapa?
    if reserva not in mapa:
        print(f"{cores['vermelho']}{estilos['negrito']}Erro: Cadeira '{reserva}' NÃO EXISTE. Tente novamente.{cores['limpa']}")
        continue # 'continue' pula de volta para o início do loop 'while'

    # 3.2 - A cadeira já foi reservada?
    if reserva in cadeiras_reservadas:
        print(f"{cores['vermelho']}{estilos['negrito']}Erro: Cadeira '{reserva}' JÁ ESTÁ RESERVADA. Tente novamente.{cores['limpa']}")
        continue # Pula de volta para o início do loop

    # --- 4. RESERVA A CADEIRA ---
    # Se o código chegou até aqui, a cadeira é válida.
    cadeiras_reservadas.append(reserva)
    print(f"{cores['verde']}{estilos['negrito']}Sucesso! Cadeira {cores['azul']}{reserva} {cores['verde']}reservada.")

    # --- 5. PERGUNTA SE QUER CONTINUAR ---
    continuar = input(f"{cores['cinza']}{estilos['negrito']}Quer reservar outro? [S/N]: ").upper()
    
    # Se o usuário digitar "N" (ou "NAO"), o 'break' para o loop 'while'
    if continuar == "N" or continuar == "NAO":
        break 

# --- FIM DO PROGRAMA ---
# Quando o loop acabar, mostra um resumo
print(f"\n{cores['amarelo']}{estilos['negrito']}Reservas finalizadas.")
print(f"{cores['cinza']}{estilos['negrito']}Suas cadeiras são:{cores['verde']}{estilos['italico']}", cadeiras_reservadas)