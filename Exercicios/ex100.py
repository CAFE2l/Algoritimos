
def media(nota1, nota2):
    """Calcula e retorna a média de duas notas"""
    return (nota1 + nota2) / 2  # RETORNA o valor numérico

def situacao(media_aluno):
    """Retorna situação baseado na média: Aprovado(>=7), Recuperação(5-6.9), Reprovado(<5)"""
    if media_aluno >= 7:
        return "APROVADO"
    elif media_aluno >= 5:
        return "RECUPERAÇÃO"
    else: 
        return "REPROVADO"

# USO CORRETO das funções
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_calculada = media(nota1, nota2)  # Chama media() e recebe o resultado
situacao_aluno = situacao(media_calculada)  # Passa resultado para situacao()

print(f"Média: {media_calculada:.1f}")
print(f"Situação: {situacao_aluno}")
