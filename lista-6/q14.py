"""
14) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a. Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
b. Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro
Escreva um programa em python algoritmo que leia: 
    o número de litros vendidos,
    o tipo de combustível (codificado da seguinte forma: A para álcool, G para gasolina), 
calcule e imprima:
    o valor a ser pago pelo cliente sabendo-se que o preço do 
    litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

products = {
    "A": [1.90, 0.03, 0.05],
    "G": [2.50, 0.04, 0.06]
}

productType = str()
productQuantity = float()
discount = float()
totalPrice = float()

print("====================")
print("  MOTA GAS STATION  ")
print("====================")
print("1 - Alcohol")
print("2 - GAS")
print("===================")

while True:
    productType = input("> Select Your Type Of Fuel: [A/G]: ").strip().upper()[0]
    if productType in products:
        break
    print("ERROR: This Product Doesn't Exist Misspelling?")
productQuantity = float(input(f"> How much {"Alcohol" if productType == "A" else "Gas"} do you need? [In Liters]:"))
totalPrice = products.get(productType)[0] * productQuantity
discount = products.get(productType)[1] if productQuantity <= 20 else products.get(productType)[2]
totalPrice -= totalPrice * discount

print("===========")
print("  PAYMENT  ")
print("===========")
print(f"> TOTAL PRICE: {totalPrice:.2f}.")
print("============")
