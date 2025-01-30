# 6.Entrar com vários números ate entrar com o numero 999. para cada numero imprimir seus divisores;

num = int ()

while True:
    num = int(input("> Enter a num [999 to stop]: "))
    if num == 999:
        print("> Stoping...")
        break
    print(f"> Num {num}. Divisors: ")
    for i in range (1, num, 1):
        if num % i == 0:
            print (i) 
