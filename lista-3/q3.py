listaFrutas = ["Morango", "Tomate", "Maracujá"]
listaDocinhos = ["Brigadeiro","Beijinho", "Doce de Leite", "Bolo"]
listaFeijoada = ["Fiejão", "Calabresa", "Cebola", "Costelinha de Porco"]
listona = [listaFrutas, listaDocinhos, listaFeijoada]

print(f"> Listona Original: {listona}.")
print(f"> Acessando Brigadeiro: {listona[1][0]}.")

# Adicionando Brigadeiros

listona[1].append("Brigadeiro")
listona[1].append("Brigadeiro")
listona[1].append("Brigadeiro")

# Adicionando bebidas

listona.append("Suco de Laranja")
listona.append("Suco de Manga")
listona.append("Suco de Uva")

# Print adicional

print(f"> Listona Após Inserções: {listona}.")