# 2.Entrar com números enquanto forem positivos, e imprimir quantos números foram digitados;

num = int ()
totalNuns = 0
while True:
    num = int(input("> Enter a num: "))
    if(num < 0):
        break
    totalNuns = totalNuns + 1

print(f"> Total of numbers: {totalNuns}.")
