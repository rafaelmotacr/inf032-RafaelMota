# 3. Entrar com um nome e imprimir: a) todo o nome; b) primeiro carcater; c) ultimo carcater; d) do primeiro
# ate o terceiro caracter; e)quarto caracter; f) os dois últimos.

nome = input("> Digite seu nome: ")
print(f"TODO O NOME: {nome}")
print(f"PRIMEIRO CARACTER: {nome[0]}")
print(f"ÚLTIMO CARACTER: {nome[-1]}")
print(f"PRIMEIRO AO TERCEIRO CARACTER: {nome[0:3]}")
print(f"QUARTO CARACTER: {nome[3]}")
print(f"DOIS ÚLTIMOS CARACTERES: {nome[-2:]}")
