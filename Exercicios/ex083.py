import random

vetor = []
for i in range(0, 20):
    vetor.append(random.randint(0, 99))
print(f"Vetor em ordem normal: {vetor}")

print(f"vetor em ordem crecente: {sorted(vetor)}")