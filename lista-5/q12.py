# 12. Entrar com dois números inteiros e efetuar a adição. Caso o valor somado seja maior que 20, este
# deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este
# deverá ser apresentado subtraindo-se 5.

num1 = int(input("> Enter the first number: "))
num2 = int(input("> Enter the second number: "))
sum = num1 + num2

if sum > 20:
    sum += 8
else :
    sum -= 5

print(f"> Sum of the numbers {sum}.")
