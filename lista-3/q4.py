listaFrutas = ["Morango", "Tomate", "Maracujá"]
listaDocinhos = ["Brigadeiro","Beijinho", "Doce de Leite", "Bolo"]
listaFeijoada = ["Fiejão", "Calabresa", "Cebola", "Costelinha de Porco"]
listona = [listaFrutas, listaDocinhos, listaFeijoada]

# Adicionando Brigadeiros

listona[1].append("Brigadeiro")
listona[1].append("Brigadeiro")
listona[1].append("Brigadeiro")

# Adicionando bebidas

listona.append("Suco de Laranja")
listona.append("Suco de Manga")
listona.append("Suco de Uva")

# Limpando listona

del listona[::-1]
print(listona)
