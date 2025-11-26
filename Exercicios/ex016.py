cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Por quantos anos você já fumou? "))

# Calcula o total de cigarros fumados
total_cigarros = cigarros * anos * 365

# Cada cigarro equivale a 10 minutos perdidos
minutos_perdidos = total_cigarros * 10

# Um dia tem 24h x 60min = 1440 minutos
dias_perdidos = minutos_perdidos / 1440

print(f"Você fumou {cigarros} por {anos} anos e perdeu aproximadamente {dias_perdidos:.2f} dias de vida.")
