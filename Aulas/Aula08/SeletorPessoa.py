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

frase = "SELETOR DE PESSOAS"

print(f"{estilos['negrito']}{cores['azul']}{"==="*5}{cores['amarelo']}PESSOAS{cores['verde']}{"==="*4}{cores['limpa']}")
print(f"{cores['cinza']}{fundo['branco']}{estilos['negrito']}{frase.center(35)}{cores['limpa']}")
print(f"{estilos['negrito']}{cores['vermelho']}{"==="*11+"=="}{cores['limpa']}") 
repost = 'S'

totHomens = 0
totMulheres = 0
while repost in 'Ss':
    sexo = str(input(f"{cores['cinza']}{estilos['negrito']}Informe o sexo da pessoa [M/F]: ")).strip().upper()[0]
    idade = str(input(f"{cores['cinza']}{estilos['negrito']}Informe a idade da pessoa: ")).strip()
    cabelo = int(input(f"{cores['cinza']}{estilos['negrito']}[1] Preto\n[2] Castanho\n[3] Loiro\n[4] Ruivo\n{cores['cinza']}{estilos['negrito']}Escolha a cor do cabelo da pessoa: "))

    if sexo == 'M' and int(idade) > 18 and cabelo == 2:
        totHomens += 1
    if sexo == "F" and idade in '25 26 27 28 29 30' and cabelo == 3:
        totMulheres += 1
    cont = str(input(f"{cores['cinza']}{estilos['negrito']}Deseja cadastrar outra pessoa?{estilos['italico']} {cores['vermelho']}[S/N]: ")).strip().upper()[0]
    repost = cont

print(f"{cores['cinza']}{estilos['negrito']}O total de homens com mais de 18 anos e cabelos catasnhos é: {estilos['italico']}{cores['azul']}{totHomens}")
print(f"{cores['cinza']}{estilos['negrito']}O total de mulheres entre 25 e 30 anos e cabelos loires é {estilos['italico']}{cores['roxo']}{totMulheres}")
print(f"{cores['verde']}{estilos['negrito']}Cadastro finalizado!")