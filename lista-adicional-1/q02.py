'''2. Assumir como constante no comando de linha do Python x = 3 e y = 6 e imprimir
usando PRINT( ) o resultado das equações seguintes:
(a) w = ex
− ln(y)
(b) z = x*y2
+ y*cos(x)


(c) s
x
y
= + ln( ) x y + + tan( ) x'''

from math import log, cos, exp, tan, sqrt

x = 3
y = 6

# A

w = math.exp(x) - math.log(y)

# B

z = x * y**2 + y * cos(x)

# C

s = sqrt(x / y + log(x + y) + tan(x))
