# 2.Entrar como nome, idade e sexo de uma pessoa. se a pessoa for do sexo feminino e tiver menos de 25
# anos, imprimir a mensagem (ACEITA), caso contrário, imprimir NAO ACEITA

name = input("> Enter your name: ")
sex = input("> Enter your biological sex [M/W]: ").upper().strip()[0]
age = int(input("> Enter your age: "))

print("> Saida: ", end = ""),
if sex != "W" and age > 25:
    print("NÃO ", end = "")
print("ACEITA")
print(".")
