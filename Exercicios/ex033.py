valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o salário do comprador? "))
anos = int(input("Em quantos ano o comprador vai pagar? "))
prestaçãoMensal = valorCasa / (anos * 12)
if (prestaçãoMensal > salario * 0.3):
    print("Empréstimo negado")
else:
    print("Empréstimo aprovado")

