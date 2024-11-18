'''7. Observar a seguinte lista de dados, lista= [2, 2, 3, 3, 3, −1, −1, −2, 0, 0, 0, 2, 4, 5, 1,
2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]. Programar o Console para encontrar as seguintes
medidas estatísticas:
(a) Soma de todos os elementos.
(b) Máximo elemento da lista.
(c) Mínimo elemento da lista.
(d) Média dos elementos da lista.
(e) Mediana dos elementos da lista.
(f) Moda dos elementos da lista.
(g) Desvio-padrão amostral.
(h) Desvio-padrão populacional.
(i) Contar o número de vezes que aparece o número 0.
(j) Contar o número de vezes que aparece o número 5.
(k) Ordenar a lista em ordem crescente.
(l) Ordenar a lista em ordem decrescente.'''

from statistics import mode, median, stdev, pstdev

lista = [2, 2, 3, 3, 3, -1, -1, -2, 0, 0, 0, 2, 4, 5, 1, 2, 2, 0, 0, 0,2 ,1, 5, 5, 7, 6, 5, 0, 0]
listaOrdenadaCrescente = lista.copy()
listaOrdenadaCrescente.sort()
listaOrdenadaDecrescente = lista.copy()
listaOrdenadaDecrescente.sort(reverse=True)

print(f"A) Soma de todos os elementos: {sum(lista)}.")
print(f"B) Máximo elemento da lista.: {max(lista)}.")
print(f"C) Mínimo elemento da lista: {min(lista)}.")
print(f"D) Média dos elementos da lista.: {sum(lista) / len(lista):.2f}.")
print(f"E) Moda dos elementos da lista: {median(lista):.2f}.")
print(f"F) Moda dos elementos da lista: {mode(lista):.2f}.")
print(f"G) Desvio-padrão amostral: {stdev(lista):.2f}.")
print(f"H) Desvio-padrão populacional: {pstdev(lista):.2f}.")
print(f"I) Contar o número de vezes que aparece o número 0: {lista.count(0)}.")
print(f"J) Contar o número de vezes que aparece o número 5: {lista.count(5)}.")
print(f"K) Ordenar a lista em ordem crescente: {listaOrdenadaCrescente}.")
print(f"L) Ordenar a lista em ordem decrescente: {listaOrdenadaDecrescente}.")
