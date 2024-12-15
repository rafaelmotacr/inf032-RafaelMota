# 9.Um comerciante comprou um produto e quer vende-lo com um lucro de 45% se o valor da compra for
# menor que 20,00, caso contrário o lucro será de 30%. entrar com o valor do produto e imprimir o valor da
# venda.

profit = int()
productValue = int(input("> Product Value: "))

if productValue > 20.00:
    profit = productValue * 0.45
else:
    profit = productValue * 0.30

sale = productValue + profit
print(f"> Sale value: {sale}.")
