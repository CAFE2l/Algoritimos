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

frase = "RECANTO ESPERANÇA"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}PROJETO{cores['verde']}{"==="*4+"="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 
print(f"{estilos['negrito']}{cores['azul']}Muito Obrigado por Ajudar{cores['limpa']}")
doacao = int(input(f"{estilos['negrito']}{cores['cinza']}[1] Para doar R$10\n[2] Para doar R$25\n[3] Para doar R$50\n[4] Para doar outro valor\n[5] Para cancelar\nEscolha a opção de doação: "))
match doacao:
    case 1:
        print(f"{estilos['negrito']}{cores['verde']}Muito obrigado por doar R$10!{cores['limpa']}")
    case 2: 
        print(f"{estilos['negrito']}{cores['verde']}Muito obrigado por doar R$25!{cores['limpa']}")
    case 3:
        print(f"{estilos['negrito']}{cores['verde']}Muito obrigado por doar R$50!{cores['limpa']}")
    case 4:
        outro_valor = int(input("Digite o valor que deseja doar: R$"))
        print(f"{estilos['negrito']}{cores['verde']}Muito obrigado por doar R${outro_valor}!{cores['limpa']}")
    case 5:
        print(f"{estilos['negrito']}{cores['vermelho']}Doação cancelada. Agradecemos sua consideração!{cores['limpa']}")
    case _:
        print(f"{estilos['negrito']}{cores['vermelho']}Opção inválida. Por favor, tente novamente.{cores['limpa']}")
print(f"{estilos['negrito']}{cores['ciano']}Obrigado por usar nossos serviços!{cores['limpa']}")