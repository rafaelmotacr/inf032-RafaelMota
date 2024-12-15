# 1. Entrar como n's números e imprimir o triplo de cada. o programa encerra quando entrar com o numero 999;

num = int ()
while True:
    num = int(input("> Enter a num: "))
    if(num == 999):
        break
    print(f"> Triple of the number: {num * 3}.")
