minhaListaDeInteiros = [2,41,13,90,11,0,34,2,41,13,90]
listaOrdenada = minhaListaDeInteiros.copy()
listaOrdenada.sort()
listaInvertida = listaOrdenada.copy()[::-1]
print(f"> Lista original: {minhaListaDeInteiros}")
print(f"> Lista ordenada: {listaOrdenada}")
print(f"> Lista ordenada invertida: {listaInvertida}")
