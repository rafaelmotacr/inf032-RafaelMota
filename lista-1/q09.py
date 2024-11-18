# supondo um retângulo de 10cm de base e 5cm de altura, imprimir a seguinte saída perímetro: / área: /
# diagonal:

from math import sqrt 

base = 10
altura = 5

perimetro = 2 * (base + altura)
area =  base * altura
diagonal = sqrt(base ** 2 + altura **2)

print('Perimetro:' + str(perimetro))
print('Área:' + str(area))
print('Diagonal:' + str(diagonal))
