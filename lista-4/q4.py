"""4. Crie um dicionário d e coloque nele seus dados: nome, idade, telefone, endereço. Usando o
dicionário d criado anteriormente, imprima seu nome."""

pessoa = {}
pessoa = {
    "nome": "Rafael",
    "idade": "21",
    "telefone": "40028922",
    "endereco": "Rua dos manos, travessa dos crias.",
}

print("Nome: " + pessoa.get("nome") + ".")
