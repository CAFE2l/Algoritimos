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

frase = "IMC CALCULATOR"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['cinza']}IMC{cores['verde']}{"==="*5+"=="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

M = float(input(f"{estilos['negrito']}{cores['cinza']}Digite sua massa em kg: "))
A = float(input(f"{cores['cinza']}{estilos['negrito']}Digite sua altura em metros: "))

IMC = M / (A ** 2)
if (IMC < 17):
    print(f"{estilos['negrito']}{cores['vermelho']}Muito abaixo do peso{cores['limpa']}")
elif (IMC >= 17 and IMC < 18.5):
    print(f"{estilos['negrito']}{cores['amarelo']}Abaixo do peso{cores['limpa']}")
elif (IMC >= 18.5 and IMC < 25):
    print(f"{estilos['negrito']}{estilos['italico']}{cores['verde']}You have the perfect body weight{cores['limpa']}")
elif (IMC >= 25 and IMC < 30):
    print(f"{estilos['negrito']}{cores['amarelo']}Acima do peso{cores['limpa']}")
elif (IMC >= 30 and IMC < 35):
    print(f"{estilos['negrito']}{cores['vermelho']}Obesidade I{cores['limpa']}")
elif (IMC >= 35 and IMC < 40):
    print(f"{estilos['negrito']}{cores['vermelho']}Obesidade II (severa){cores['limpa']}")
else: 
    print(f"{estilos['negrito']}{cores['vermelho']}Obesidade III (mórbida){cores['limpa']}")