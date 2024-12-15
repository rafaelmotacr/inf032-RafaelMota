# 4.Entrar com vários números e informar quantos números entre 100 e 200 foram digitados. quando o valor 0 for digitado o programa deve encerrar;

num = int()
totalInRange = 0 

while True:
    num = int(input("> Enter a num: "))
    if num > 100 and num < 200:
        totalInRange = totalInRange + 1
    elif num == 0:
        break

print(f"> Numbers between 100 and 200: {totalInRange}.")
