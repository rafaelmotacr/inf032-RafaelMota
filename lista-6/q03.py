# 3.Entrar com vários números positivos e imprimir a media dos números digitados. o programa acaba quando se informar que não deseja mais continuar.

exit = False
sumOfNumbers = 0
totalNumbers = int()
question = str()

while not exit:
    num = int(input("> Enter a num: "))
    question = input("> Do you want to continue? [Y/n]: ").strip().upper()
    if question == 'N':
        exit = True
    sumOfNumbers = sumOfNumbers + num
    totalNumbers = totalNumbers + 1

print(f"> Numbers Average: {sumOfNumbers/totalNumbers}.")
