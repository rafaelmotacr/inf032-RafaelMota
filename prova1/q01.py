"""
1) Sabendo-se que a UAL calcula a divisão através de subtrações sucessivas, criar m
programa que calcule e imprima o resto da divisão de números inteiros lidos. suponha
que os números lidos sejam positivos e que o dividendo seja maior que o divisor.

"""

while True:
    dividendo = int(input("> Digite o Dividendo: "))
    if dividendo <= 0:
        print("> ERRO: O dividendo deve ser um número positivo maior que zero!")
        continue
    break


while True:   
    divisor = int(input("> Digite o Divisor: "))
    if divisor > dividendo or divisor <= 0:
        print("> ERRO: o divisor deve ser maior que zero e menor que o dividendo!")
        continue
    break


dividendoTMP = dividendo
while dividendoTMP >= divisor:
    dividendoTMP -= divisor

resto = dividendoTMP    
print(f"> O resto da divisão de {dividendo} por {divisor} é {resto}.")
