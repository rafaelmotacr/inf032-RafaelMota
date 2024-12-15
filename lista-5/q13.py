# 13. Entrar com um número e escrever uma das mensagens: “é múltiplo de 3", ou "não é múltiplo de 3"

num = int(input("> Enter a num: "))
if num % 3 == 0:
    print("> The number is a multiple of three!")
else:
    print("> The number isn't a multiple of three!")
