# 7. uma figura cujo ângulo e 80 graus. Imprima o seno, co-seno, tangente, secante, cp-secante, e co-tangente.

import math

rad = math.radians(80)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
cossecante = 1 / seno
cotangente = 1 / tangente
secante = 1 / cosseno

print('SENO = ' + str(seno))
print('COSSENO = ' + str(cosseno))
print('TANGENTE = ' + str(tangente))
print('COSSECANTE = ' + str(cossecante))
print('COTANGENTE = ' + str(cotangente))
print('SECANTE = ' + str(secante))
