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

frase = "ESCOLA SANTA PACIENCIA"

print(f"{estilos['negrito']}{cores['azul']}{"==="*3+"="}{cores['amarelo']}SANTA-PACIENCIA{cores['verde']}{"==="*3+"="}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 

alunos = int(input(f"{cores['cinza']}{estilos['negrito']}Digite o número de alunos na sala: {cores['limpa']}"))
if alunos <= 0:
    print(f"{estilos['negrito']}{cores['vermelho']}Nenhum aluno para processar.{cores['limpa']}")
else:
    melhor = None
    pior = None
    maior = float("-inf")
    menor = float("inf")

    for i in range(1, alunos + 1):
        nome = input(f"{estilos['negrito']}{cores['verde']}Digite o nome do {i}º aluno: {cores['limpa']}")
        while True:
            try:
                nota = float(input(f"{estilos['negrito']}{cores['verde']}Digite a nota do {i}º aluno: {cores['limpa']}"))
                break
            except ValueError:
                print(f"{cores['vermelho']}{estilos['negrito']}Entrada inválida. Digite um número para a nota.{cores['limpa']}")

        if nota > maior:
            maior = nota
            melhor = nome
        if nota < menor:
            menor = nota
            pior = nome

    print(f"{estilos['negrito']}{cores['ciano']}O aluno com a maior nota é {melhor} com a nota {maior}{cores['limpa']}")
    print(f"{estilos['negrito']}{cores['ciano']}O aluno com a menor nota é {pior} com a nota {menor}{cores['limpa']}")