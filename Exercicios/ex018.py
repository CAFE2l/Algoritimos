nascimento = int(input(f"Em que ano você nasceu? "))
idade = 2025 - nascimento
if (idade >= 18):
    print(f"Com {idade} anos você já pode votar")
else:
    print(f"Com {idade} anos você ainda não pode votar")