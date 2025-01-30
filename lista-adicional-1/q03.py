'''3. Criar a lista de números num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2] e fatiá-la con-
forme os itens a seguir:

(a) Fatiar do elemento de índice 2 ao de índice 3.
(b) Fatiar do quinto elemento ao nono elemento.
(c) Fatiar do elemento de índice 1 ao último.
(d) Fatiar do primeiro elemento ao último.
(e) Fatiar do primeiro elemento ao último saltando de três em três elementos.
(f) Selecionar o último elemento da lista.
(g) Selecionar os três últimos elementos da lista.
(h) Selecionar os quatro primeiros elementos da lista.
(i) Contar o número de elementos da lista.
(j) Contar quantas vezes aparece o número 1 na lista.'''

num=[3, 3, 4, 1, 2, 1, 1, 2, 3, 4, 4, 1, 1, 5, 2]

print(f"A) {num[2:3]}.")
print(f"B) {num[4:8]}.")
print(f"C) {num[1:]}.")
print(f"D) {num[:]}.")
print(f"E) {num[::4]}.")
print(f"F) {num[-1]}.")
print(f"G) {num[-3:]}.")
print(f"H) {num[:4]}.")
print(f"I) {len(num)}.")
print(f"J) {num.count(1)}.")
