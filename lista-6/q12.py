# 12) Faça um Programa para uma loja de tintas. O programa deverá
# pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 
# 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# • Informe ao usuário as quantidades de tinta a serem compradas e os 
# respectivos preços em 3 situações:
# • comprar apenas latas de 18 litros;
# • comprar apenas galões de 3,6 litros;
# • misturar latas e galões, de forma que o preço seja o menor. 

def priceByProduct(capacity,neededInk,costPerUnity):
    productNeeded = int(neededInk / capacity) 
    remainingInk = neededInk % capacity
    if remainingInk > 0:
        productNeeded += 1
    return productNeeded * costPerUnity 


def priceUsingCansAndGallons(neededInk = float()):

    remainingInk = neededInk
    inkCans = inkGallons = int()

    if remainingInk >= 18: 
        inkCans = int(remainingInk / 18) 
        remainingInk = remainingInk % 18

    if remainingInk >= 3.6:
        inkGallons = int(remainingInk / 3.6)
        remainingInk = remainingInk % 3.6

    if remainingInk > 0:
        inkGallons += 1

    priceMixed = inkCans * 80 + inkGallons * 25
    return priceMixed


# Main

totalArea = float(input("> Enter the size of the area: "))
remainingInk = neededInk = totalArea / 6

print(f"> You'll need {neededInk:.2f} liters of ink, that will cust: ")
print(f"# Using Only Cans (R$ 80 Each): R${priceByProduct(18, neededInk, 80)}.")
print(f"# Using Only Gallons (R$ 25 Each): R${priceByProduct(3.6, neededInk, 25)}.")
print(f"# Using Both (Most Economic): R$ {priceUsingCansAndGallons(neededInk)}.")
