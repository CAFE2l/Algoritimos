def ProximoFibonacci(A, B):
    # Calcula o próximo termo da sequência
    C = A + B
    print(C)     # Exibe o novo termo
    A = B        # Atualiza A para o próximo ciclo
    B = C        # Atualiza B para o próximo ciclo
    return A, B  # Retorna os novos valores para atualização

T1 = 0
T2 = 1

print(T1)  # Exibe o primeiro termo (opcional)
print(T2)  # Exibe o segundo termo (opcional)

# Gera e exibe termos do 3º ao 10º
for C in range(3, 11):    # inclui o 10º termo
    T1, T2 = ProximoFibonacci(T1, T2)  # Atualiza T1 e T2 com os retornos da função
