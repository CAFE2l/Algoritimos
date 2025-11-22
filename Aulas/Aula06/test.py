
bangu = int(input("Quantos Gols do Bangu?"))
madureira = int(input("Quantos Gols do Madureira?"))

diferenca = bangu - madureira

if diferenca > 4:
    print(f"DIFERENÇA:  {diferenca}")
    print("STATUS:  GOLEADA")
elif diferenca < -4:
    print(f"DIFERENÇA:  {abs(diferenca)}")
    print("STATUS:  GOLEADA{cores['limpa']}")
elif diferenca == 0:
    print(f"DIFERENÇA: {diferenca}")
    print("STATUS: EMPATE!")
else:
    print(f"DIFERENÇA:  {abs(diferenca)}")
    print(f"STATUS: PARTIDA NORMAL")