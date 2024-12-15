# 10. Dada a frase “Python é muito legal". use fatiamento para dar nome às variáveis contendo cada palavra.
# Qual o tamanho dessa frase? E qual o tamanho de cada palavra?

frase  = "Python é muito legal"
palavra1 = frase[0:6]
palavra2 = frase[7]
palavra3 = frase[9:14]
palavra4 = frase[15:]
print(f"> Tamanho da frase: {len(frase)}.")
print(f"> Tamanho palavra 1 ({palavra1}): {len(palavra1)}.")
print(f"> Tamanho palavra 2 ({palavra2}): {len(palavra2)}.")
print(f"> Tamanho palavra 3 ({palavra3}): {len(palavra3)}.")
print(f"> Tamanho palavra 4 ({palavra4}): {len(palavra4)}.")
