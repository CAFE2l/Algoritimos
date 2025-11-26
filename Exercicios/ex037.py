salarioAtual = float(input("Digite seu salário atual: "))
sexo = str(input("Digite seu sexo [M/F]: ")).upper()
anos = int(input("A quantos anos vc trabalha na empresa? "))

if (sexo == "F" and anos <= 15):
    aumento = salarioAtual * 0.05
    novoSalario = salarioAtual + aumento
    print(f"Seu novo salário é: {novoSalario}")
elif (sexo == "F" and anos > 15 and anos <= 20):
    aumento = salarioAtual * 0.12
    novoSalario = salarioAtual + aumento
    print(f"Seu novo salário é: {novoSalario}")
elif (sexo == "F" and anos > 20):
    aumento = salarioAtual * 0.23
    novosalario = salarioAtual + aumento
    print(f"Seu novo salário é: {novosalario}")
elif (sexo == "M" and anos < 20):
    aumento = salarioAtual * 0.03
    novoSalario = salarioAtual + aumento
    print(f"Seu novo salário é: {novoSalario}")
elif (sexo == "M" and anos > 20 and anos <= 30):
    aumento = salarioAtual * 0.13
elif (sexo == "M" and anos > 30):
    aumento = salarioAtual * 0.25