# 5.Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caracter de cada nome;

nameList = list()
name = str()

while True:
    name = input("> Enter a name: ")
    if name.upper() == "FIM":
        break
    nameList.append(name)

for tmp in nameList:
    print(f"> {tmp[0]}") 
