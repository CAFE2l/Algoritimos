melhoresAlunos = []
vetor = []
for i in range(1, 10):
    nota = float(input(f"Digite a nota do {i} aluno: "))
    vetor.append(nota)  

    media = sum(vetor) / len(vetor)
    maiorNota = max(vetor)
    
    if(nota > media):
        melhoresAlunos.append(i)


print(f"As notas maiores que a média foram estão nas posições:  {melhoresAlunos}")
print(f"A média da turma foi: {media:.1f}")

print(f"A maior nota digita foi: {maiorNota} na posição {vetor.index(maiorNota)}")