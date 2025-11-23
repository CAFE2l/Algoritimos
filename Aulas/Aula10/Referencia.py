def soma(a, b):
    a += 1
    b += 2
    return a, b

x = 4
y = 8
x, y = soma(x, y)
print(f"valor de x: {x}")
print(f"valor de y: {y}")
