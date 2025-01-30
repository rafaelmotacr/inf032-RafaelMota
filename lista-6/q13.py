"""
13) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

Até 5 Kg                   Acima de 5 Kg
File Duplo R$ 4,90 por Kg  R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg     R$ 6,80 por Kg
Picanha R$ 6,90 por Kg     R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
promoção, porém não há limites para a quantidade de carne por cliente. 

Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.

Escreva um programa que peça: 

tipo
quantidade de carne

E gere um cupom fiscal, contendo as informações de:

tipo e quantidade de carne, 
preço total,
tipo de pagamento, 
valor do desconto e 
valor a pagar.
"""

typeOfMeat = str()
meatAmmount = float()
paymentMethod = int()
meatOptions = {
    "1":[4.90, 5.80, "File Duplo"],
    "2":[5.90, 6.80, "Alcatra"],
    "3":[6.90, 7.80, "Picanha"]
}

discount = float(0)
price = float() 
priceWithDiscout = float()

print("===================")
print("  TABAJARA MARKET  ")
print("===================")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")
print("===================")

typeOfMeat = input("> Select The Type of Meat [1/2/3]: ")
meatAmount = float(input("> How Much Meat do you Want? [In Kilograms]: "))

print("===========")
print("  PAYMENT  ")
print("===========")
print("1 - Money")
print("2 - Tabajara Card ")
print("============")

paymentMethod = int(input("> Select The Payment Method: "))

if meatAmount > 5:
    price = (meatOptions.get(typeOfMeat)[1] * 5) + (meatOptions.get(typeOfMeat)[0] * (meatAmount - 5))
else:
    price = meatOptions.get(typeOfMeat)[0] * meatAmount

priceWithDiscout = price

if paymentMethod == 2:
    discount = price * 0.05
    priceWithDiscout -= discount
    
print("============")
print("  Checkout  ")
print("============")
print(f"PRODUCT(s): 1 x {meatAmount} kilogram(s) of {meatOptions.get(typeOfMeat)[2]}.")
print(f"TOTAL PRICE: R$ {str(price).replace(".", ",")}.")
print(f"PAYMENT METHOD: {"Money" if paymentMethod == 1 else "Tabajara Card"}.")
print(f"DISCOUNT VALUE: R$ {str(discount).replace(".", ",")}.")
print(f"AMOUNT TO BE PAID: R$ {str(priceWithDiscout).replace(".", ",")}")
