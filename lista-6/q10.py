# 10.Criar um programa que deixe entrar com 10 números positivos
# e imprima a raiz quadrada de cada numero. para cada entrada 
# de dados devera haver um trecho de "proteção" para que um numero negativo não seja aceito.

from math import sqrt

numberList = list()
number = int()

while len(numberList) < 10:
    number = int(input("> Enter a number: "))
    if number < 0:
        print("\033[31mERROR: THE NUMBER SHOULD BE POSITIVE. TRY AGAIN.\033[m")
        continue
    numberList.append(number)

print("====================================")

for num in numberList:
    print(f"> Square Root of {num} = {sqrt(num)}.")
