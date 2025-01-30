# 15.A prefeitura do Rio de Janeiro abriu uma linha de crédito para seus funcionários. O valor máximo da
# prestação não poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o
# salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

salary = float(input("> Enter Your Salary: "))
installment = float(input("> What is the value of the installment?: "))

if installment > salary * 0.30:
    print("> Loan not granted.")
else:
    print("> Loan granted.")
