# 4. Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de
# aulas dadas; c) percentual de desconto INSS.

valorHora = float(input("> VAlOR HORA AULA: "))
aulasDadas = int(input("> NUMERO DE AULAS: "))
descontoINSS = float(input("> DESCONTO INSS: "))

# 1 aula 1 hour
valorBruto = valorHora * aulasDadas
salarioLiquido = float( valorBruto - (valorBruto * (descontoINSS / 100)) )
print(f"> SALÁRIO LÍQUIDO: {salarioLiquido}.")
