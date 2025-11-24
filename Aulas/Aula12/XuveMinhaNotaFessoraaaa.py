# --- 1. GABARITO ---
# (Mudei os nomes para g_q1 (gabarito_questao1) para não confundir)
print("--- CADASTRO DO GABARITO ---")
g_q1 = input(f"Gabarito Questão 1: ")
g_q2 = input(f"Gabarito Questão 2: ")
g_q3 = input(f"Gabarito Questão 3: ")
g_q4 = input(f"Gabarito Questão 4: ")
g_q5 = input(f"Gabarito Questão 5: ")

# --- 2. LISTAS VAZIAS ---
# Vamos guardar os nomes e as notas finais aqui
lista_nomes_alunos = []
lista_notas_alunos = []

# --- 3. LOOP DOS ALUNOS ---
# O 'range(0, 3)' vai rodar o código 3 vezes (para o aluno 0, 1 e 2)
for i in range(0, 3):
    
    # Usamos (i + 1) para mostrar "Aluno 1", "Aluno 2", etc.
    print(f"\n--- Aluno {i + 1} ---") 
    
    # Pede o nome do aluno e guarda na lista de nomes
    nome = input("Digite o nome do aluno: ")
    lista_nomes_alunos.append(nome)
    
    # ZERA a nota para cada novo aluno
    nota_final = 0 
    
    print(f"RESPOSTAS DADAS PELO(A) {nome}")
    
    # --- 4. CORREÇÃO DA PROVA ---
    
    # Pede a resposta do aluno e guarda em uma NOVA variável (resp1)
    resp1 = input(f"Questão 1: ")
    # Compara a resposta do aluno (resp1) com o gabarito (g_q1)
    if resp1 == g_q1:
        nota_final += 1 # Se for igual, soma 1 ponto

    # (Eu adicionei a Questão 2 que estava faltando)
    resp2 = input(f"Questão 2: ")
    if resp2 == g_q2:
        nota_final += 1

    resp3 = input(f"Questão 3: ")
    if resp3 == g_q3:
        nota_final += 1

    resp4 = input(f"Questão 4: ")
    if resp4 == g_q4:
        nota_final += 1

    resp5 = input(f"Questão 5: ")
    if resp5 == g_q5:
        nota_final += 1

    # --- 5. GUARDA A NOTA ---
    # Depois de corrigir as 5 questões, adiciona (append) a nota final 
    # do aluno na lista de notas
    lista_notas_alunos.append(nota_final)
    print(f"A nota do(a) {nome} foi: {nota_final}/5")


# --- 6. RESULTADO FINAL ---
# No final de tudo, mostra as duas listas
print("\n--- RESULTADO FINAL ---")
print(f"Alunos: {lista_nomes_alunos}")
print(f"Notas:  {lista_notas_alunos}")