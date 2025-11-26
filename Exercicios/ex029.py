nome = str(input("Digite o nome do funcionário: "))
salario = float(input("Digite o salário do funcionário: "))
anos  = int(input("Digite quantos anos o funcionário trabalha na empresa: "))

if (anos <= 3):
    aumento = salario * 0.03
    novoSalario = salario + aumento
    print(f"O novo salário deste funcionário deve ser: {novoSalario}")
elif (anos > 3 and anos <= 10):
    aumento = salario * 0.125
    novoSalario = salario + aumento
    print(f"O novo salário deste funcionário deve ser: {novoSalario}")
else: 
    aumento = salario * 0.20
    novoSalario = salario + aumento
    print(f"O novo salário deste funcionário deve ser: {novoSalario}")