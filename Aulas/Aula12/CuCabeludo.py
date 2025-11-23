# Lista para armazenar nomes que começam com 'C'
soCuCabeludo = []
tot = 0

# Lê 10 nomes e verifica se começam com 'C' ou 'c'
for c in range(0, 10):
    # O input() já retorna uma string, não é necessário o str()
    nome = input("Digite seu nome: ") 
    
    # .strip() remove espaços em branco antes ou depois do nome
    # .upper() transforma o nome em maiúsculo (ex: "carlos" vira "CARLOS")
    # .startswith("C") verifica se o nome transformado começa com "C"
    if nome.strip().upper().startswith("C"):
        tot += 1                  # Conta quantos nomes começam com 'C'
        soCuCabeludo.append(nome)  # Adiciona o nome original ao final da lista

# Exibe todos os nomes que começaram com 'C'
print("\n--- Nomes que começam com 'C' ---")
for nome in soCuCabeludo:
    print(nome)

# (Opcional) Exibe o total de nomes encontrados
print(f"Total de nomes encontrados: {tot}")