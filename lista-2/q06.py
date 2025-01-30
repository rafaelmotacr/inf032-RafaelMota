# 6. Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que
# calcule o valor da prestação.

valorEmprestimo = float(input("> Digite o valor do empréstimo: "))
taxaJuros = float(input("> Taxas de juros: "))
quantidadeMeses = float(input("> Parcelas: "))
valorParcela = valorEmprestimo * (taxaJuros * 0.1) / quantidadeMeses
print(f"Valor das parcelas: {valorParcela:.2f}")
