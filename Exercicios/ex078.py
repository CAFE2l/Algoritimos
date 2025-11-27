vetor = []
for i in range(0, 101):
    if (i % 10 == 0):
        test = (f"[{i}]")
        vetor.append(test)
    else: 
        vetor.append(i)
print(vetor)