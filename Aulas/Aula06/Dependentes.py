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

frase = "DEPENDENCIAS DE UM FUNCIONÁRIO"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}FUNCIONARIO{cores['verde']}{"==="*3}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 


Nome = str(input(f"{estilos['negrito']}{cores['cinza']}Digite o nome do funcionário: {cores['limpa']}"))
Sal = float(input(f"{estilos['negrito']}{cores['cinza']}Digite o salário do funcionário: R$ {cores['limpa']}"))
NumDep = int(input(f"{estilos['negrito']}{cores['cinza']}Digite o número de dependentes: {cores['limpa']}"))

match NumDep:
    case 0:
        NovoSal = Sal + (Sal * 0.05)
    case 1 | 2 | 3:
        NovoSal = Sal + (Sal * 0.10)
    case 4 | 5 | 6:
        NovoSal = Sal + (Sal * 0.15)
    case _:
        NovoSal = Sal + (Sal * 0.20)

print(f"{estilos['negrito']}{cores['cinza']}O funcionário {cores['verde']}{Nome}{cores['cinza']} com {cores['vermelho']}{NumDep} dependente(s) {cores['cinza']}terá um novo salário de {cores['verde']}R$ {NovoSal:.2f}")